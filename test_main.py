import pytest
from main import Context, UpperCase, LowerCase, TitleCase, SwapCase, CapitalizeCase

def test_uppercase_strategy():
    context = Context(UpperCase())
    assert context.get_result("hello world!") == "HELLO WORLD!"
    assert context.get_result("Hello World!") == "HELLO WORLD!"

def test_lowercase_strategy():
    context = Context(LowerCase())
    assert context.get_result("HELLO WORLD!") == "hello world!"
    assert context.get_result("Hello World!") == "hello world!"

def test_titlecase_strategy():
    context = Context(TitleCase())
    assert context.get_result("hello world!") == "Hello World!"
    assert context.get_result("hELLO wORLD!") == "Hello World!"

def test_swapcase_strategy():
    context = Context(SwapCase())
    assert context.get_result("hEllo wORld!") == "HeLLO WorLD!"
    assert context.get_result("HELLO world!") == "hello WORLD!"

def test_capitalize_strategy():
    context = Context(CapitalizeCase())
    assert context.get_result("hello world!") == "Hello world!"
    assert context.get_result("HELLO WORLD!") == "Hello world!"

def test_context_set_strategy():
    context = Context(UpperCase())
    assert context.get_result("hello world!") == "HELLO WORLD!"
    context.set_strategy(LowerCase())
    assert context.get_result("HELLO WORLD!") == "hello world!"
    context.set_strategy(CapitalizeCase())
    assert context.get_result("hello world!") == "Hello world!"
    context.set_strategy(SwapCase())
    assert context.get_result("hEllo wORld!") == "HeLLO WorLD!"
    context.set_strategy(TitleCase())
    assert context.get_result("hello world!") == "Hello World!"

if __name__ == "__main__":
    pytest.main()
