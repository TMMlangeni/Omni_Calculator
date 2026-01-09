class Calculation:
    def __init__(self,time, operation, input_data, result):
        self.time = time
        self.operation = operation
        self.input_data = input_data
        self.result = result

    def __str__(self):
        return f"Result: {self.result}"