from .dal.repositories.hevy_api import HevyAPI
from .common.env_config import EnvConfig
from .model import Workout1

def main():
    print("Hello from hevy-ai-assist!")

config: EnvConfig = EnvConfig()

if __name__ == "__main__":
    main()
    
    api = HevyAPI(
        base_url=config.HEVY_API_URL,
        auth_key=config.HEVY_API_KEY
    )
    
    result = api.get_workouts_list(page=1, page_size=10)

    workout_list_dict = result.get("workouts", [])
    
    # Convert the list of dictionaries to a list of Workout objects
    workout_list = [Workout1(**workout) for workout in workout_list_dict]

    work1 = workout_list[0]
    
    by_id = api.get_workout_by_id(work1.id)
    print(result)