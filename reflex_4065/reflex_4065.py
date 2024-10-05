import reflex as rx


class State(rx.State):
    public_var: str = ""
    _private_var: str = ""

    def update_variables(self):
        self.public_var = "hello"
        self._private_var = "world"

    @rx.var
    def private_var(self):
        return self._private_var
    
    def clear(self):
        self.reset()


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Test case for Issue 4064", size="9"),
            rx.button(
                'Set public variable to "hello" and private variable to "world" ',
                on_click=State.update_variables,
            ),
            rx.button(
                "Reset state",
                on_click=State.clear,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.text(f'public variable is: "{State.public_var}"'),
        rx.text(f'private variable is: "{State.private_var}"'),
    )


app = rx.App()
app.add_page(index)
