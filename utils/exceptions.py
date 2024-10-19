class ForceExit(Exception):
    def __init__(self, message: str, error_code: int = 1):
        super().__init__(message)  # Call the base class constructor
        self.error_code = error_code  # Store additional error information

    def __str__(self):
        return f"{self.args[0]} (Error code: {self.error_code})"