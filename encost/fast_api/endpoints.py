import asyncio
from functools import partial

from asgiref.sync import sync_to_async
from fast_api.models import EndpointStates
from fast_api.schemas import Schema, EndpointStatesFA
from fastapi import APIRouter

from encost.settings import ENDPOINT_ID, MULTIPLE_OF

router = APIRouter()


def prepare_asnwer(states: list[EndpointStates], multiple_of: int):
    """
    Подготовка ответа на тестовое задание:

    -input_start равный "2023-12-20T22:39:40.000"
    a. Найти все записи из endpoint_state где state_start >= input_start
    и endpoint_id = 139
    b. Отсортировать данные по state_start desc.
    c. Из данных, полученных в b, найти все записи, где id строки
    кратен числу 3
    d. В ответ роут в формате json возвращает: “filtered_count” –
    количество полученных записей, "client_info" – поле info из
    связанно модели clients_info у третьей записи из списка пункта
    c., "state_id" - state_id у третьей записи.
    """
    endpoint_states = [
        element for index, element in enumerate(states)
        if not (index + 1) % multiple_of]
    result = {
        "len_states": len(endpoint_states),
        "client_info": endpoint_states[2].client.client_info.info,
        "state_id": endpoint_states[2].state_id}
    return result


@router.post("/endpoint_states")
def get_endpoint_states(input_start: Schema):
    """ Возвращаем ответ синхронно. """
    endpoint_states = EndpointStates.objects.select_related("client").filter(
        state_start__gte=input_start.input_start,
        endpoint_id=ENDPOINT_ID,
        ).order_by('-state_start')
    result = prepare_asnwer(endpoint_states, MULTIPLE_OF)
    return result


@router.post("/endpoint_states_async")
async def get_endpoint_states_async(input_start: Schema):
    """ Возвращаем ответ асинхронно. """
    endpoint_states = EndpointStates.objects.select_related("client").filter(
        state_start__gte=input_start.input_start,
        endpoint_id=ENDPOINT_ID,
        ).order_by('-state_start')
    func = sync_to_async(partial(prepare_asnwer, endpoint_states, MULTIPLE_OF))

    result = await asyncio.create_task(func())
    return result


@router.get("/endpoints_states/")
def get_items(limit: int = 10, offset: int = 0):
    """
    Получить список элементов EndpointStatesFA с пагинацией.

    :param limit: Количество элементов на странице (по умолчанию: 10)
    :param offset: Смещение для пагинации (по умолчанию: 0)
    :return: Список элементов cthbfkbpjdfyysq знвфтеш
    """
    endpoint_states = EndpointStates.objects.select_related("client").all()
    result = [
        EndpointStatesFA(
            endpoint_states_id=item.id, 
            endpoint_id=item.endpoint.id,
            client_id=item.client.id,
            state_name=item.state_name,
            state_reason=item.state_reason,
            state_start=item.state_start,
            state_end=item.state_end,
            state_id=item.state_id,
            group_id=item.group_id,
            reason_group=item.reason_group,
            info=item.info
            )
        for item in endpoint_states
        ]
    return result[offset: limit + offset]
