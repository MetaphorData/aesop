from rich.console import Console


class MetaphorConsole(Console):
    def ok(self, message: str):
        return self.print(message, style="green")

    def warning(self, message: str):
        return self.print(message, style="bold yellow")

    def error(self, message: str):
        return self.print(message, style="bold red")


console = MetaphorConsole()