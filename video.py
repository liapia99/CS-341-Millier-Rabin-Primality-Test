from manim import *

class ShowWrite(Scene):
    def construct(self):
        # Create the text
        text = Tex("Miller-Rabin Primality Test").scale(1)

        # Add the text to the scene and animate writing
        self.play(Write(text))

        # Wait for 5 seconds
        self.wait(2)

        # Animate unwriting the text
        self.play(Unwrite(text))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class NumberGrid(Scene):
    def construct(self):
        grid_size = 10
        spacing = 0.7  # Adjust spacing for better fit
        font_size = 18  # Reduce font size

        # Zoom out the camera to fit the entire grid
        self.camera.frame_width = 12 # Correct way to adjust camera zoom

        numbers = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                num = i * grid_size + j
                color = ORANGE if is_prime(num) else WHITE
                text = Text(str(num), font_size=font_size, color=color)
                text.move_to(np.array([(j - grid_size / 2) * spacing, (grid_size / 2 - i) * spacing, 0]))
                numbers.add(text)

        self.play(Create(numbers), run_time=5)
        self.wait(5)


class UsingIndicate(Scene):
    def construct(self):
        tex1 = Tex("Determines if a number is ")
        tex2 = Tex("Prime")
        tex_group = VGroup(tex1, tex2).arrange(RIGHT)

        self.play(Write(tex1))
        self.wait()
        self.play(Indicate(tex2))
        self.wait()


