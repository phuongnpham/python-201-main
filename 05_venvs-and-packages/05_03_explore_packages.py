import typer

def greet(name: str, age: int):
    print(f"Hello {name}! You are {age} years old.")

if __name__ == "__main__":
    typer.run(greet)