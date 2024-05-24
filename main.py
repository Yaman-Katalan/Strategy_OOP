from abc import ABC, abstractmethod


# Interface
class Strategy(ABC):
    @abstractmethod
    def set_text_case(self, text:str) -> str:
        pass


# Concrete Classes
class UpperCase(Strategy):
    def set_text_case(self, text:str) -> str:
        return text.upper()
    
class LowerCase(Strategy):
    def set_text_case(self, text:str) -> str:
        return text.lower()
    
class TitleCase(Strategy):
    def set_text_case(self, text: str) -> str:
        return text.title()
    
class SwapCase(Strategy):
    def set_text_case(self, text: str) -> str:
        return text.swapcase()
    
class CapitalizeCase(Strategy):
    def set_text_case(self, text: str) -> str:
        return text.capitalize()

# Context

class Context:
    def __init__(self, strategy:Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy:Strategy):
        self.strategy = strategy

    def get_result(self, text:str):
        return self.strategy.set_text_case(text)


context = Context(UpperCase())
print(context.get_result("hello world!"))

context = Context(LowerCase())
print(context.get_result("hello world!"))

context.set_strategy(CapitalizeCase())
print(context.get_result("hello world!"))

context.set_strategy(SwapCase())
print(context.get_result("hEllo wORld!"))

context.set_strategy(TitleCase())
print(context.get_result("hello world!"))