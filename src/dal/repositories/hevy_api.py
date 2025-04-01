from uplink import Consumer, get, Path, Query, returns
from uplink.auth import ApiTokenHeader

class HevyAPI(Consumer):
    
    def __init__(self, base_url: str, auth_key: str):
        api_key_auth: ApiTokenHeader = ApiTokenHeader(header="api-key", token=auth_key)
        super().__init__(base_url=base_url, auth=api_key_auth)
    
    # TODO -> implement correct response schema for each request
    # TODO -> implement the post/put requests
    
    @returns.json
    @get("/v1/workouts")
    def get_workouts_list(self,page: Query("page") = 1, page_size: Query("pageSize") = 10):  # type: ignore
        """
        Get a list of workouts.
        
        Args:
            page (int): The page number to retrieve.
            per_page (int): The number of workouts per page.

        Returns:
            List[dict]: A list of workouts.
        """
    
    @returns.json
    @get("/v1/workouts/count")
    def get_workouts_count(self):  
        """
        Get the count of workouts.
        
        Returns:
            int: The total number of workouts.
        """
        
    @returns.json
    @get("/v1/workouts/{workoutid}")
    def get_workout_by_id(self, workout_id: Path("workoutid")):   # type: ignore
        """
        Get a specific workout by its ID.
        
        Args:
            workoutid (str): The ID of the workout.

        Returns:
            dict: The workout details.
        """
        
    @returns.json
    @get("/v1/routines")
    def get_routines_list(self, page: Query("page") = 1, page_size: Query("pageSize") = 10): # type: ignore
        """
        Get a list of routines.
        
        Args:
            page (int): The page number to retrieve.
            per_page (int): The number of routines per page.

        Returns:
            List[dict]: A list of routines.
        """
        
    @returns.json
    @get("/v1/exercise_templates")
    def get_exercise_template_list(self, page: Query("page") = 1, page_size: Query("pageSize") = 10): # type: ignore
        """
        Get a paginated list of exercise templates available on the account.
        
        Args:
            page (int): The page number to retrieve.
            per_page (int): The number of exercise templates per page.

        Returns:
            List[dict]: A list of exercise templates.
        """
        
    @returns.json
    @get("/v1/exercise_templates/{exerciseTemplateId}")
    def get_exercise_template_by_id(self, exercise_template_id: Path("exerciseTemplateId")): # type: ignore
        """
        Get a specific exercise template by its ID.
        
        Args:
            exerciseTemplateId (str): The ID of the exercise template.

        Returns:
            dict: The exercise template details.
        """
        
    @returns.json
    @get("/v1/routine_folders")
    def get_routine_folder_list(self, page: Query("page") = 1, page_size: Query("pageSize") = 10): # type: ignore
        """
        Get a list of routine folders.
        
        Args:
            page (int): The page number to retrieve.
            per_page (int): The number of routine folders per page.

        Returns:
            List[dict]: A list of routine folders.
        """
        
    @returns.json
    @get("/v1/routine_folders/{folderId}")
    def get_routine_folder_by_id(self, routine_folder_id: Path("folderId")): # type: ignore
        """
        Get a specific routine folder by its ID.
        
        Args:
            folderId (str): The ID of the routine folder.

        Returns:
            dict: The routine folder details.
        """