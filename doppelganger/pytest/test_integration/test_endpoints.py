'''
This script tests the configuration of the environment file,
the availability of the Ollama server, and the models
loaded into memory

Functions:
    check_environment_file(filepath: str) -> bool:
        Verifies if the environment file exists and
           checks if the necessary values are set
           correctly
        Args:
            filepath (str): The path of the environment file
        Returns:
            bool: True if the file exists and values are correct,
                False otherwise
        Raises:
            FileNotFoundError: If the environment file does not exist
            ValueError: If the environment file contains invalid values

    check_ollama_server(url: str) -> bool:
        Checks if the Ollama server is running and accessible
            through the provided URL
        Args:
            url (str): API endpoint
        Returns:
            bool: True if the server is accessible, False otherwise
        Raises:
            ConnectionError: If the server is not accessible within the
                specified timeout
            HTTPError: If the server responds with an unexpected
                status code

    check_models_loaded([models] : list) -> bool:
        Ensures that the required models are loaded into memory
        Args:
            models (list[str]): A list of model names expected
             to be loaded into memory.
        Returns:
            bool: True if the list contains all models in memory
                False otherwise
        Raises:
            ValueError: If the model list is empty or invalid
            PartialModelLoadError: If only some models are loaded
'''
