from constants import *


config.background_color = WHITE


class ArithmeticOperators(Scene):
    def construct(self):
        title = Text("Arithmetic Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'Addition  ( + )',
            'Subtraction ( - )',
            'Multiplication ( * )',
            'Division ( / )',
            'Modulus ( % )',
            'Exponent ( ** )',
            'Floor Division ( // )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 3) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 2) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))
            self.wait(2)

        self.wait(90)


class ComparisonOperators(Scene):
    def construct(self):
        title = Text("Comparison Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'Equal to  ( == )',
            'Not equal to    ( != )',
            'Greater than ( > )',
            'Less than ( < )',
            'Greater than or equal to ( >= )',
            'Less than or equal to ( <= )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 3) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 2) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)


class AssignmentOperators(Scene):
    def construct(self):
        title = Text("Assignment Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'Assign  ( == )',
            'Add and assign    ( += )',
            'Subtract and assign ( -= )',
            'Multiply and assign ( *= )',
            'Divide and assign ( /= )',
            'Modulus and assign ( %= )',
            'Exponentiation and assign ( **= )',
            'Floor division and assign ( //= )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 2.5) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 1.6) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)


class LogicalOperators(Scene):
    def construct(self):
        title = Text("Logical Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'Logical AND  ( and )',
            'Logical OR    ( or )',
            'Logical NOT ( not )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 2.5) - index * 1) * UP).shift((FRAME_X_RADIUS // 1.6) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)


class BitwiseOperators(Scene):
    def construct(self):
        title = Text("Bitwise Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'Bitwise AND  ( and )',
            'Bitwise OR    ( or )',
            'Bitwise XOR / exclusive OR ( ^ )',
            'Bitwise NOT ( not )',
            'Left shift ( << )',
            'Right shift ( >> )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 2.5) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 1.6) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)


class MembershipOperators(Scene):
    def construct(self):
        title = Text("Membership Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'in  ( Returns True if value is in sequence )',
            'not in    ( Returns True if value is not in sequence )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 2.5) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 1.6) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)


class IdentityOperators(Scene):
    def construct(self):
        title = Text("Identity Operators", font_size=40, color=BLACK)
        self.play(Create(title, run_time=0.0001))
        self.play(title.animate.shift((FRAME_Y_RADIUS - 1) * UP))
        self.wait(20)

        # List of arithmetic operators
        operators = [
            'is         ( True if both variables point to the same object )',
            'is  not    ( True if both variables do not point to the same object )',
        ]

        for index, text in enumerate(operators):
            dot = Dot(color=BLACK).move_to(((FRAME_Y_RADIUS / 2.5) - index * 0.7) * UP).shift((FRAME_X_RADIUS // 1.6) * LEFT)
            text = Text(text, font_size=20, color=BLACK).next_to(dot)
            self.play(Create(dot, run_time=0.1), Create(text, run_time=0.2))

        self.wait(90)

