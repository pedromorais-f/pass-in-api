from src.models.repository.check_ins_repository import CheckInsRepository
from src.models.repository.attendees_repository import AttendeesRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.errors_types.http_not_found import HttpNotFound

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_repository = CheckInsRepository()
        self.__attendees_repository = AttendeesRepository()
    
    #Method to do an attendee`s check in
    def register(self, http_request: HttpRequest) -> HttpResponse:
        check_in_info = http_request.get_param["attendee_id_info"]
        try:
            attendee = self.__attendees_repository.get_attendee_by_id(check_in_info)
            self.__check_in_repository.insert_check_in(check_in_info)

            return HttpResponse(body={
                "check_in":{
                    "name": attendee.name,
                    "id": attendee.id
                }
            }, status_code=201)
        except Exception:
            raise HttpNotFound('The attendee do not exist!')