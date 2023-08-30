import pyparsing as pp

greet = pp.Word(pp.upper) + "," + pp.Word(pp.upper) + "!"
for greeting_str in [
    "HELLO, WORLD!",
    "HI, THERE!",
    "HEY, EVERYONE!",
]:
    greeting = greet.parse_string("Hello world")
    print(greeting)
    