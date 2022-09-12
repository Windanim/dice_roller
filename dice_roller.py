import flet
from flet import Page, Row, Text, icons, colors, buttons, Container
from random import randint

class DiceRoller:

    def __init__(self, page_object) -> None:

        self.page_object = page_object
        self.die_list = ['20', '12', '100', '10', '8', '6', '4']
        self.current_die_index = 0
        self.current_title = Text(value=str('D' + self.die_list[self.current_die_index]), text_align="center", width=500, size=45, weight="bold")

        self.current_image = flet.Image(
                        src=f"/diceVector_d" + str(self.die_list[self.current_die_index]) + ".png",
                        width=200,
                        height=200,
                        fit="contain"
                    )

        self.current_die_state = Text(value=str(self.die_list[self.current_die_index]), text_align="center", width=100, color="red", size=30, weight="bold")

        # I NEED TO DEFINE A CONTAINER HERE

        self.page_object.add( # I NEED TO REMOVE THIS
            Row( # THIS NEEDS TO BE SHIFTED INTO THE CONTAINER
                [
                    self.current_title
                ],
                alignment='center'
            )
        )

        self.page_object.add( # I NEED TO REMOVE THIS
            Row( # THIS NEEDS TO BE SHIFTED INTO THE CONTAINER
                [
                    flet.ElevatedButton('<', on_click=self.minus_click, style=flet.ButtonStyle(shape=buttons.CircleBorder())),
                    flet.Stack(
                        [
                            self.current_image,
                            Container(content=self.current_die_state,
                                alignment=flet.alignment.center
                            )
                        ],
                        height=200,
                        width=200
                    ),
                    flet.ElevatedButton('>', on_click=self.plus_click, style=flet.ButtonStyle(shape=buttons.CircleBorder())),
                ],
                alignment="center",
            )
        )

        self.page_object.add( # I NEED TO REMOVE THIS
            Row( # THIS NEEDS TO BE SHIFTED INTO THE CONTAINER
                [
                    flet.ElevatedButton('Roll', on_click=self.roll_click),
                ],
                alignment="center",
            )
        )

    def minus_click(self, e):

        if self.current_die_index > 0:
            self.current_die_index -= 1
        else:
            self.current_die_index = int(len(self.die_list) - 1)

        self.current_title.value = str('D' + self.die_list[self.current_die_index])
        self.current_image.src = f"/diceVector_d" + str(self.die_list[self.current_die_index]) + ".png"
        self.current_die_state.value = str(self.die_list[self.current_die_index])
        self.page_object.update() # THE ACCESS FOR THIS FUNCTION NEEDS TO BE REDIFINED IN ORDER TO ACCOMODATE FOR MORE DYNAMIC / MODULAR CALLS

    def plus_click(self, e):

        if self.current_die_index < int(len(self.die_list) - 1):
            self.current_die_index += 1
        else:
            self.current_die_index = 0

        self.current_title.value = str('D' + self.die_list[self.current_die_index])
        self.current_image.src = f"/diceVector_d" + str(self.die_list[self.current_die_index]) + ".png"
        self.current_die_state.value = str(self.die_list[self.current_die_index])
        self.page_object.update() # THE ACCESS FOR THIS FUNCTION NEEDS TO BE REDIFINED IN ORDER TO ACCOMODATE FOR MORE DYNAMIC / MODULAR CALLS

    def roll_click(self, e):

        self.current_die_state.value = str(randint(1, int(self.die_list[self.current_die_index])))
        self.page_object.update() # THE ACCESS FOR THIS FUNCTION NEEDS TO BE REDIFINED IN ORDER TO ACCOMODATE FOR MORE DYNAMIC / MODULAR CALLS

def main(app_page: Page):

        app_page.title = "DnD Dice Roller"
        app_page.vertical_alignment = "center"
        app_page.window_height = 1000
        app_page.window_width = 1500
        initial_die = DiceRoller(app_page)
        second_die = DiceRoller(app_page)

flet.app(target=main, assets_dir='images')
#flet.app(target=main, assets_dir='images', view=flet.WEB_BROWSER)