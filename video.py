from manim import *
import numpy as np

class TitleScene(Scene):
    def construct(self):
        # Main title
        title = Tex("Miller-Rabin Primality Algorithm").scale(1.5)
        subtitle = Tex("A Probabilistic Primality Test").scale(0.8)
        subtitle1 = Tex("Julia Piascik \\& Bolen Alfreh").scale(0.5)
        subtitle.next_to(title, DOWN)
        subtitle1.next_to(subtitle, DOWN)
        # Create a group for the title and subtitle
        title_group = VGroup(title, subtitle, subtitle1)
        title_group.move_to(ORIGIN)
        
        # Animate the title
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait(2)
        self.play(Write(subtitle1))
        self.wait(2)
        # Fade out
        self.play(FadeOut(title_group))

class WhatItDoesScene(Scene):
    def construct(self):
        # First part: Centered title
        main_text = Tex("The Miller-Rabin test determines if a number is PRIME").scale(1.0)
        main_text.move_to(ORIGIN)
        
        # Animate the first part
        self.play(Write(main_text))
        self.wait(7)
        
        # Fade out first part
        self.play(FadeOut(main_text))
        
        # Second part: Function diagram and bullet points
        # Function diagram
        function = Tex("$f(n)$").scale(1.5)
        prime_text = Tex("Prime").scale(0.8)
        composite_text = Tex("Composite").scale(0.8)
        self.wait(15)

        # Position elements
        function.move_to(ORIGIN)
        prime_text.move_to(UP + RIGHT * 2)
        composite_text.move_to(DOWN + RIGHT * 2)
        
        # Create arrows
        prime_arrow = Arrow(function.get_right(), prime_text.get_left(), buff=0.2)
        composite_arrow = Arrow(function.get_right(), composite_text.get_left(), buff=0.2)
        
        # Bullet points (removed first point)
        bullet_point1 = Tex("- Can never prove a number is prime just if the number ", "is not prime")
        self.wait(5)
        bullet_point2 = Tex("- If it fails to prove a number is not prime, then it most likely is prime")
        
        # Highlight "is not prime" in yellow
        bullet_point1[1].set_color(YELLOW)
        
        bullet_points = VGroup(bullet_point1, bullet_point2).arrange(DOWN, aligned_edge=LEFT)
        bullet_points.scale(0.8)
        bullet_points.next_to(function, DOWN, buff=1.5)
        bullet_points.to_edge(LEFT, buff=1)
        
        # Animate the second part
        self.play(Write(function))
        self.play(
            Write(prime_text),
            Write(composite_text),
            Create(prime_arrow),
            Create(composite_arrow)
        )
        self.wait(3)
        
        # Move everything up together
        diagram_group = VGroup(function, prime_text, composite_text, prime_arrow, composite_arrow)
        self.play(
            diagram_group.animate.shift(UP * 1.5)
        )
        self.play(Write(bullet_points))
        self.wait(20)
        
        # Fade out everything
        self.play(
            FadeOut(diagram_group),
            FadeOut(bullet_points)
        )

class CarmichaelAndEuclidScene(Scene):
    def construct(self):
        # Carmichael Numbers section
        carmichael_title = Tex("2. Carmichael Numbers").scale(1.2)
        carmichael_title.move_to(ORIGIN)
        
        # Animate title
        self.play(Write(carmichael_title))
        self.wait(1)
        
        # Move title to top
        self.play(carmichael_title.animate.to_edge(UP))
        
        # Definition
        definition = Tex("A Fermat pseudoprime to any base $a$ with $\\gcd(a,n) = 1$").scale(0.8)
        definition.next_to(carmichael_title, DOWN, buff=1)
        
        # Animate definition
        self.play(Write(definition))
        self.wait(2)
        
        # Fade out definition
        self.play(FadeOut(definition))
        
        # Example 1
        carmichael_example1 = VGroup(
            Tex("Example 1:"),
            Tex("$2^{340} \\equiv 1 \\pmod{341}$"),
            Tex("But $341 = 11 \\cdot 31$ is composite"),
            Tex("341 is a Fermat pseudoprime to base 2")
        ).arrange(DOWN, aligned_edge=LEFT)
        carmichael_example1.scale(0.8)
        carmichael_example1.next_to(carmichael_title, DOWN, buff=1)
        
        # Animate first example
        self.play(Write(carmichael_example1))
        self.wait(3)
        
        # Fade out first example
        self.play(FadeOut(carmichael_example1))
        
        # Example 2
        carmichael_example2 = VGroup(
            Tex("Example 2:"),
            Tex("$5^{560} \\equiv 1 \\pmod{561}$"),
            Tex("But $561 = 3 \\cdot 11 \\cdot 17$ is composite"),
            Tex("561 is a Fermat pseudoprime to base 5")
        ).arrange(DOWN, aligned_edge=LEFT)
        carmichael_example2.scale(0.8)
        carmichael_example2.next_to(carmichael_title, DOWN, buff=1)
        
        # Animate second example
        self.play(Write(carmichael_example2))
        self.wait(3)
        
        # Fade out second example
        self.play(FadeOut(carmichael_example2))
        
        # Warning text
        warning = Tex("If someone is supposed to provide us with a prime\\\\ number, and sends a Carmichael number instead,\\\\ we cannot detect it with the Fermat test.").scale(0.8)
        warning.next_to(carmichael_title, DOWN, buff=1)
        
        # Animate warning
        self.play(Write(warning))
        self.wait(3)
        
        # Fade out everything
        self.play(
            FadeOut(carmichael_title),
            FadeOut(warning)
        )
        
        # Euclid's Lemma section
        euclid_title = Tex("3. Euclid's Lemma").scale(1.2)
        euclid_title.move_to(ORIGIN)
        
        # Animate title
        self.play(Write(euclid_title))
        self.wait(1)
        
        # Move title to top
        self.play(euclid_title.animate.to_edge(UP))
        
        # Statement
        statement = Tex("If a prime $p$ divides the product of two numbers $(x \\cdot y)$,\\\\ it must divide at least one of those numbers.").scale(0.8)
        statement.next_to(euclid_title, DOWN, buff=1)
        
        # Animate statement
        self.play(Write(statement))
        self.wait(2)

        # Example
        example = VGroup(
            Tex("Example:"),
            Tex("Let $x = 12$, $y = 8$ and $p = 3$"),
            Tex("$p$ divides the product $12 \\cdot 8 = 96$"),
            Tex("$p$ also divides $12$"),
            Tex("Since $p$ is prime, it must be completely\\\\ present in either $x$ or $y$")
        ).arrange(DOWN, aligned_edge=LEFT)
        example.scale(0.8)
        example.next_to(statement, DOWN, buff=1)
        
        # Animate example
        self.play(Write(example))
        self.wait(3)
        
        # Fade out everything
        self.play(
            FadeOut(euclid_title),
            FadeOut(statement),
            FadeOut(example)
        )

class BackgroundScene(Scene):
    def construct(self):
        # Initial question
        question = Tex("How does the test work?").scale(1.2)
        question.move_to(ORIGIN)
        
        # Animate question
        self.play(Write(question))
        self.wait(5)
        self.play(FadeOut(question))
        
        # Fermat's Little Theorem
        fermat_title = Tex("1. Fermat's Little Theorem").scale(1.2)
        fermat_title.move_to(ORIGIN)
        
        # Animate title
        self.play(Write(fermat_title))
        self.wait(1)
        
        # Move title to top
        self.play(fermat_title.animate.to_edge(UP))
        
        # Theorem statements
        theorem1 = Tex("If $a^{n-1} \\not\\equiv 1 \\pmod{n}$ for some $a$ with $a \\not\\equiv 0 \\pmod{n}$,\\\\ then $n$ is composite.").scale(0.8)
        theorem1.next_to(fermat_title, DOWN, buff=1)
        
        # Animate first theorem
        self.play(Write(theorem1))
        self.wait(2)
        
        # Second theorem statement
        theorem2 = Tex("OR").scale(0.8)
        theorem2.next_to(theorem1, DOWN, buff=0.5)
        
        theorem3 = Tex("If $n$ is a prime number, then for every $a$, $1 < a < n-1$\\\\ $a^{n-1} \\equiv 1 \\pmod{n}$ and $a^{n-1} - 1 \\equiv 0 \\pmod{n}$").scale(0.8)
        theorem3.next_to(theorem2, DOWN, buff=0.5)
        
        # Animate second theorem
        self.play(Write(theorem2))
        self.play(Write(theorem3))
        self.wait(3)
        
        # Fade out theorems
        self.play(
            FadeOut(theorem1),
            FadeOut(theorem2),
            FadeOut(theorem3)
        )
        
        # Example 1: n = 4
        example1 = VGroup(
            Tex("Testing $n = 4$"),
            Tex("Choose $a = 2$ (since $1 < a < 3$)"),
            Tex("$2^{3} - 1 = 8 - 1 = 7$"),
            Tex("$7 \\div 4 = 1.75$"),
            Tex("Since $4$ does not divide $7$, $4$ is composite")
        ).arrange(DOWN, aligned_edge=LEFT)
        example1.scale(0.8)
        example1.next_to(fermat_title, DOWN, buff=1)
        
        # Animate first example
        self.play(Write(example1))
        self.wait(3)
        
        # Fade out first example
        self.play(FadeOut(example1))
        
        # Example 2: n = 7
        example2 = VGroup(
            Tex("Testing $n = 7$"),
            Tex("Choose $a = 3$ (since $1 < a < 6$)"),
            Tex("$3^{6} - 1 = 729 - 1 = 728$"),
            Tex("$728 \\div 7 = 104$"),
            Tex("Since $7$ divides $728$, $7$ is probably prime")
        ).arrange(DOWN, aligned_edge=LEFT)
        example2.scale(0.8)
        example2.next_to(fermat_title, DOWN, buff=1)
        
        # Animate second example
        self.play(Write(example2))
        self.wait(5)

        # Fade out everything
        self.play(
            FadeOut(fermat_title),
            FadeOut(example2)
        )
        
        # Carmichael Numbers section
        carmichael_title = Tex("2. Carmichael Numbers").scale(1.2)
        carmichael_title.move_to(ORIGIN)
        self.play(Write(carmichael_title))
        self.wait(1)
        self.play(carmichael_title.animate.to_edge(UP))

        # Definition
        definition = Tex("A Fermat pseudoprime to any base $a$ with $\\gcd(a,n) = 1$").scale(0.8)
        definition.next_to(carmichael_title, DOWN, buff=1)
        self.play(Write(definition))
        self.wait(2)
        self.play(FadeOut(definition))

        # Example 1
        carmichael_example1 = VGroup(
            Tex("Example 1:"),
            Tex("$2^{340} \\equiv 1 \\pmod{341}$"),
            Tex("But $341 = 11 \\cdot 31$ is composite"),
            Tex("341 is a Fermat pseudoprime to base 2")
        ).arrange(DOWN, aligned_edge=LEFT)
        carmichael_example1.scale(0.8)
        carmichael_example1.next_to(carmichael_title, DOWN, buff=1)
        self.play(Write(carmichael_example1))
        self.wait(3)
        self.play(FadeOut(carmichael_example1))

        # Example 2
        carmichael_example2 = VGroup(
            Tex("Example 2:"),
            Tex("$5^{560} \\equiv 1 \\pmod{561}$"),
            Tex("But $561 = 3 \\cdot 11 \\cdot 17$ is composite"),
            Tex("561 is a Fermat pseudoprime to base 5")
        ).arrange(DOWN, aligned_edge=LEFT)
        carmichael_example2.scale(0.8)
        carmichael_example2.next_to(carmichael_title, DOWN, buff=1)
        self.play(Write(carmichael_example2))
        self.wait(3)
        self.play(FadeOut(carmichael_example2))

        # After the second example, clear everything including title
        self.play(FadeOut(carmichael_example2), FadeOut(carmichael_title))
        self.wait(0.5)

        # Warning text on blank screen
        warning = Tex("If someone is supposed to provide us with a prime\\\\ number, and sends a Carmichael number instead,\\\\ we cannot detect it with the Fermat test.").scale(0.8)
        warning.move_to(ORIGIN)
        self.play(Write(warning))
        self.wait(3)
        self.play(FadeOut(warning))

        # Euler Test section
        euler_title = Tex("3. The Euler Test").scale(1.2)
        euler_title.move_to(ORIGIN)
        self.play(Write(euler_title))
        self.wait(1)
        self.play(euler_title.animate.to_edge(UP))

        # Statement
        euler_statement = VGroup(
            Tex("If $n$ is an odd prime, we know that an integer can have at most two\\\\ square roots, mod $n$. In particular, the only square roots of 1 (mod $n$)\\\\ are $\\pm 1$."),
            Tex("If $a \\not\\equiv 0$ (mod $n$), $a^{(n-1)/2}$ is a square root of $a^{n-1} \\equiv 1$ (mod $n$),\\\\ so $a^{(n-1)/2} \\equiv \\pm 1$ (mod $n$)."),
            Tex("If $a^{(n-1)/2} \\not\\equiv \\pm 1$ (mod $n$) for some $a$ with $a \\not\\equiv 0$ (mod $n$),\\\\ then $n$ is composite.")
        ).arrange(DOWN, aligned_edge=LEFT)
        euler_statement.scale(0.8)
        euler_statement.move_to(ORIGIN)
        self.play(Write(euler_statement))
        self.wait(3)
        self.play(FadeOut(euler_statement))

        # Test procedure
        test_procedure = VGroup(
            Tex("For a randomly chosen $a$ with $a \\not\\equiv 0$ (mod $n$), compute\\\\ $a^{(n-1)/2}$ (mod $n$)."),
            Tex("i) If $a^{(n-1)/2} \\equiv \\pm 1$ (mod $n$), declare $n$ a probable prime,\\\\ and optionally repeat the test a few more times."),
            Tex("If $n$ is large and chosen at random, the probability that $n$\\\\ is prime is very close to 1."),
            Tex("ii) If $a^{(n-1)/2} \\not\\equiv \\pm 1$ (mod $n$), declare $n$ composite."),
            
        ).arrange(DOWN, aligned_edge=LEFT)
        test_procedure.scale(0.8)
        test_procedure.move_to(ORIGIN)
        self.play(Write(test_procedure))
        self.wait(3)
        self.play(FadeOut(test_procedure))

        # Examples
        example1 = VGroup(
            Tex("Example 1:"),
            Tex("$2^{170} \\equiv 1$ (mod 341) (even though 340 is composite)"),
            Tex("341 is a Euler pseudoprime to base 2")
        ).arrange(DOWN, aligned_edge=LEFT)
        example1.scale(0.8)
        example1.move_to(ORIGIN)
        self.play(Write(example1))
        self.wait(3)
        self.play(FadeOut(example1))

        example2 = VGroup(
            Tex("Example 2:"),
            Tex("$5^{280} \\equiv 67 \\not\\equiv \\pm 1$ (mod 561)"),
            Tex("This test shows that 561 is composite"),
            Tex("561 is not prime according to the Euler test")
        ).arrange(DOWN, aligned_edge=LEFT)
        example2.scale(0.8)
        example2.move_to(ORIGIN)
        self.play(Write(example2))
        self.wait(3)
        self.play(FadeOut(example2), FadeOut(euler_title))

        # Limitation on blank screen
        limitation = Tex("The limitation of the Euler test is that it does not go to any special\\\\ effort to find square roots of 1, different from $\\pm 1$.").scale(0.8)
        limitation.move_to(ORIGIN)
        self.play(Write(limitation))
        self.wait(3)
        self.play(FadeOut(limitation))

        # Euclid's Lemma section
        euclid_title = Tex("4. Euclid's Lemma").scale(1.2)
        euclid_title.move_to(ORIGIN)
        self.play(Write(euclid_title))
        self.wait(1)
        self.play(euclid_title.animate.to_edge(UP))

        # Statement
        statement = Tex("If a prime $p$ divides the product of two numbers $(x \\cdot y)$,\\\\ it must divide at least one of those numbers.").scale(0.8)
        statement.next_to(euclid_title, DOWN, buff=1)
        self.play(Write(statement))
        self.wait(2)
        
        # Example
        euclid_example = VGroup(
            Tex("Example:"),
            Tex("Let $x = 12$, $y = 8$ and $p = 3$"),
            Tex("$p$ divides the product $12 \\cdot 8 = 96$"),
            Tex("$p$ also divides $12$"),
            Tex("Since $p$ is prime, it must be completely\\\\ present in either $x$ or $y$")
        ).arrange(DOWN, aligned_edge=LEFT)
        euclid_example.scale(0.8)
        euclid_example.next_to(statement, DOWN, buff=1)
        self.play(Write(euclid_example))
        self.wait(3)
        
        # Fade out everything
        self.play(
            FadeOut(euclid_title),
            FadeOut(statement),
            FadeOut(euclid_example)
        )

class HowItWorksScene(Scene):
    def construct(self):
        # Initial title centered
        title = Tex("The Miller-Rabin Test ").scale(1.2)
        title.move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # First text block
        text1 = VGroup(
            Tex("Recall $n$ is prime if and only if the solutions of $x^2 \\equiv 1 \\pmod{n}$\\\\ are $x \\equiv \\pm 1$"),
            Tex("So, if $n$ passes the Fermat test, that is, $a^{n-1} \\equiv 1$,"),
            Tex("then we also check $\\frac{a^{n-1}}{2} \\equiv \\pm 1$, because $\\frac{a^{n-1}}{2}$\\\\ is a square root of 1.")
        ).arrange(DOWN, center=True, buff=1.2)
        text1.scale(0.8)
        text1.move_to(ORIGIN + UP * 0.5)
        self.play(Write(text1))
        self.wait(3)
        self.play(FadeOut(text1))

        # "But what if it's a large number?" title
        title2 = Tex("But what if it's a large number?").scale(1.2)
        title2.move_to(ORIGIN)
        self.play(Write(title2))
        self.wait(2)
        self.play(FadeOut(title2))

        # "Or what if it's a Carmichael number?" title
        title3 = Tex("Or what if it's a Carmichael number?").scale(1.2)
        title3.move_to(ORIGIN)
        self.play(Write(title3))
        self.wait(2)
        self.play(FadeOut(title3))

        # Explanation text
        text2 = VGroup(
            Tex("We continue halving the exponent until we reach a number besides 1."),
            Tex("If it's anything but $-1$ then $n$ must be composite."),
            Tex("If $n$ is prime, this sequence begins with 1 and either:"),
            Tex("1. Every member is 1, or"),
            Tex("2. The first member of the sequence not equal to 1 is $-1$")
        ).arrange(DOWN, center=True, buff=1.2)
        text2.scale(0.8)
        text2.move_to(ORIGIN)
        self.play(Write(text2))
        self.wait(3)
        self.play(FadeOut(text2))

        # Zn definition
        zn_title = Tex("$a \\in \\mathbb{Z}_n$").scale(1.2)
        zn_title.move_to(ORIGIN + UP * 0.5)
        self.play(Write(zn_title))
        self.wait(1)
        
        zn_def = Tex("$\\mathbb{Z}_n = \\{0, 1, 2, \\ldots, n-1\\}$").scale(0.8)
        zn_condition = Tex("$1 < a < n-1$").scale(0.8)
        zn_group = VGroup(zn_def, zn_condition).arrange(DOWN, buff=0.3)
        zn_group.next_to(zn_title, DOWN)
        self.play(Write(zn_group))
        self.wait(2)
        
        # Express n-1 as 2^k * m
        express = Tex("Express $n-1$ as $2^k \\cdot m$ where $m$ is odd").scale(0.8)
        express.next_to(zn_condition, DOWN, buff=0.3)
        self.play(Write(express))
        self.wait(2)

        # Sequence of powers
        powers = Tex("$a^m, a^{2m}, a^{4m}, \\dots, a^{2^k m} = a^{n-1}$").scale(0.8)
        powers.next_to(express, DOWN, buff=0.3)
        self.play(Write(powers))
        self.wait(2)

        # Clear screen - fade out everything together
        self.play(
            FadeOut(zn_title),
            FadeOut(zn_group),
            FadeOut(express),
            FadeOut(powers)
        )

        # Equation sequence
        eq1_term1 = Tex("$(\\frac{a^{n-1}}{2} - 1)$").scale(0.8)
        eq1_term2 = Tex("$(\\frac{a^{n-1}}{2} + 1)$").scale(0.8)
        eq1_end = Tex("$\\equiv 0 \\pmod{n}$").scale(0.8)
        
        eq1_group = VGroup(eq1_term1, eq1_term2, eq1_end).arrange(RIGHT, buff=0.1)
        eq1_group.move_to(ORIGIN)
        
        self.play(Write(eq1_group))
        self.wait(1)

        # Add brace under first term
        brace1 = Brace(eq1_term1, DOWN)
        even = Tex("Even").scale(0.6)
        even.next_to(brace1, DOWN)
        self.play(Create(brace1), Write(even))
        self.wait(1)
        self.play(FadeOut(even))

        # Second equation
        eq2_term1 = Tex("$(\\frac{a^{n-1}}{4} - 1)$").scale(0.8)
        eq2_term2 = Tex("$(\\frac{a^{n-1}}{4} + 1)$").scale(0.8)
        eq2_term3 = Tex("$(\\frac{a^{n-1}}{2} + 1)$").scale(0.8)
        eq2_end = Tex("$\\equiv 0 \\pmod{n}$").scale(0.8)
        
        eq2_group = VGroup(eq2_term1, eq2_term2, eq2_term3, eq2_end).arrange(RIGHT, buff=0.1)
        eq2_group.next_to(eq1_group, DOWN, buff=1.5)
        
        self.play(Write(eq2_group))
        self.wait(1)

        # Add second brace
        brace2 = Brace(eq2_term1, DOWN)
        self.play(Create(brace2))
        self.wait(1)

        # Move both equations and braces up
        self.play(
            eq1_group.animate.shift(UP),
            eq2_group.animate.shift(UP),
            brace1.animate.shift(UP),
            brace2.animate.shift(UP)
        )

        # Third equation
        eq3 = Tex("$(\\frac{a^{n-1}}{8} - 1)(\\frac{a^{n-1}}{8} + 1)(\\frac{a^{n-1}}{4} + 1)(\\frac{a^{n-1}}{2} + 1) \\equiv 0 \\pmod{n}$").scale(0.8)
        eq3.next_to(eq2_group, DOWN, buff=1.0)
        self.play(Write(eq3))
        self.wait(2)
        self.play(FadeOut(eq1_group), FadeOut(eq2_group), FadeOut(eq3), FadeOut(brace1), FadeOut(brace2))

        # General form
        general = Tex("$(\\frac{a^{n-1}}{2^k} - 1)(\\frac{a^{n-1}}{2^k} + 1) \\cdots (\\frac{a^{n-1}}{2} + 1) \\equiv 0 \\pmod{n}$").scale(0.8)
        general.move_to(ORIGIN)
        self.play(Write(general))
        self.wait(2)
        self.play(FadeOut(general))

        # Clear screen
        self.play(FadeOut(general))
        self.wait(0.5)

        # Example with 341
        title = Tex("Example with 341").scale(1.2)
        title.move_to(ORIGIN)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(0.5)

        # Step 1
        step1_line1 = Tex("\\textbf{Step 1: Express } $n - 1 = 340 = 2^2 \\cdot 85$").scale(0.8)
        step1_line1.move_to(ORIGIN)
        self.play(Write(step1_line1))
        self.wait(1)
        self.play(step1_line1.animate.shift(UP * 1.5))
        
        step1_line2 = Tex("$\\Rightarrow k = 2, \\quad m = 85$").scale(0.8)
        step1_line2.next_to(step1_line1, DOWN, buff=0.5)
        self.play(Write(step1_line2))
        self.wait(1)
        
        # Step 2
        step2 = Tex("\\textbf{Step 2: Choose a base } $a = 2$").scale(0.8)
        step2.next_to(step1_line2, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(1)
        
        # Clear screen
        self.play(FadeOut(step1_line1), FadeOut(step1_line2), FadeOut(step2))
        self.wait(0.5)
        
        # Step 3
        step3_title = Tex("\\textbf{Step 3: Compute successive powers } $a^{2^k \\cdot m} \\mod 341$").scale(0.8)
        step3_title.move_to(ORIGIN)
        self.play(Write(step3_title))
        self.wait(1)
        self.play(step3_title.animate.shift(UP * 2))
        
        # Show powers one by one without moving them up
        powers = [
            Tex("$2^{85} \\equiv 32 \\pmod{341}$").scale(0.8),
            Tex("$2^{2 \\cdot 85} \\equiv 32^2 \\equiv 1 \\pmod{341}$").scale(0.8),
            Tex("$2^{4 \\cdot 85} \\equiv 1^2 \\equiv 1 \\pmod{341}$").scale(0.8)
        ]
        
        # Position each power below the previous one
        for i, power in enumerate(powers):
            if i == 0:
                power.move_to(ORIGIN)
            else:
                power.next_to(powers[i-1], DOWN, buff=0.5)
            self.play(Write(power))
            self.wait(0.5)
        
        # Clear screen
        self.play(FadeOut(step3_title), *[FadeOut(power) for power in powers])
        self.wait(0.5)
        
        # Step 4 - Keep everything centered
        step4_title = Tex("\\textbf{Step 4: Apply the general form}").scale(0.8)
        step4_title.move_to(ORIGIN + UP * 2)  # Move title up
        self.play(Write(step4_title))
        self.wait(1)
        
        step4_formula = Tex("$\\left( \\frac{a^{n-1}}{2^k} - 1 \\right)\\left( \\frac{a^{n-1}}{2^k} + 1 \\right) \\cdots \\left( \\frac{a^{n-1}}{2} + 1 \\right) \\equiv 0 \\pmod{n}$").scale(0.8)
        step4_formula.next_to(step4_title, DOWN, buff=0.5)
        self.play(Write(step4_formula))
        self.wait(1)
        
        step4_calculation = Tex("$\\left(2^{85} - 1\\right)\\left(2^{85} + 1\\right)\\left(2^{170} + 1\\right) = (31)(33)(2) \\mod 341 = 0$").scale(0.8)
        step4_calculation.next_to(step4_formula, DOWN, buff=0.5)
        self.play(Write(step4_calculation))
        self.wait(1)
        
        step4_conclusion = Tex("\\textbf{Since } $2^{85} \\equiv 32 \\not\\equiv \\pm 1 \\mod 341$, $341$ is composite").scale(0.8)
        step4_conclusion.next_to(step4_calculation, DOWN, buff=0.5)
        self.play(Write(step4_conclusion))
        self.wait(2)
        
        # Clear screen
        self.play(FadeOut(step4_title), FadeOut(step4_formula), FadeOut(step4_calculation), FadeOut(step4_conclusion))
        self.wait(0.5)

        # Example with 104513
        title = Tex("Example with 104513").scale(1.2)
        title.move_to(ORIGIN)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(0.5)

        # Step 1
        step1_line1 = Tex("\\textbf{Step 1: Express } $n - 1 = 104512 = 2^6 \\cdot 1633$").scale(0.8)
        step1_line1.move_to(ORIGIN)
        self.play(Write(step1_line1))
        self.wait(1)
        self.play(step1_line1.animate.shift(UP * 1.5))
        
        step1_line2 = Tex("$\\Rightarrow k = 6, \\quad m = 1633$").scale(0.8)
        step1_line2.next_to(step1_line1, DOWN, buff=0.5)
        self.play(Write(step1_line2))
        self.wait(1)
        
        # Step 2
        step2 = Tex("\\textbf{Step 2: Choose a base } $a = 3$").scale(0.8)
        step2.next_to(step1_line2, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(1)
        
        # Clear screen
        self.play(FadeOut(step1_line1), FadeOut(step1_line2), FadeOut(step2))
        self.wait(0.5)
        
        # Step 3
        step3_title = Tex("\\textbf{Step 3: Compute successive powers } $a^{2^k \\cdot m} \\mod 104513$").scale(0.8)
        step3_title.move_to(ORIGIN)
        self.play(Write(step3_title))
        self.wait(1)
        self.play(step3_title.animate.shift(UP * 3))  # Move title higher
        
        # Show powers one by one without moving them up
        powers = [
            Tex("$3^{1633} \\equiv 88958 \\pmod{104513}$").scale(0.8),
            Tex("$3^{2 \\cdot 1633} \\equiv 88958^2 \\equiv 10430 \\pmod{104513}$").scale(0.8),
            Tex("$3^{4 \\cdot 1633} \\equiv 10430^2 \\equiv 91380 \\pmod{104513}$").scale(0.8),
            Tex("$3^{8 \\cdot 1633} \\equiv 91380^2 \\equiv 29239 \\pmod{104513}$").scale(0.8),
            Tex("$3^{16 \\cdot 1633} \\equiv 29239^2 \\equiv 2781 \\pmod{104513}$").scale(0.8),
            Tex("$3^{32 \\cdot 1633} \\equiv 2781^2 \\equiv -1 \\pmod{104513}$").scale(0.8),
            Tex("$3^{64 \\cdot 1633} \\equiv (-1)^2 \\equiv 1 \\pmod{104513}$").scale(0.8)
        ]
        
        # Position each power below the previous one with less spacing
        for i, power in enumerate(powers):
            if i == 0:
                power.move_to(ORIGIN + UP * 1.5)  # Start higher
            else:
                power.next_to(powers[i-1], DOWN, buff=0.3)  # Reduced spacing
            self.play(Write(power))
            self.wait(0.5)
        
        # Clear screen
        self.play(FadeOut(step3_title), *[FadeOut(power) for power in powers])
        self.wait(0.5)
        
        # Step 4 - Keep everything centered
        step4_title = Tex("\\textbf{Step 4: Apply the general form}").scale(0.8)
        step4_title.move_to(ORIGIN + UP * 2)  # Move title up
        self.play(Write(step4_title))
        self.wait(1)
        
        step4_formula = Tex("$\\left( \\frac{a^{n-1}}{2^k} - 1 \\right)\\left( \\frac{a^{n-1}}{2^k} + 1 \\right) \\cdots \\left( \\frac{a^{n-1}}{2} + 1 \\right) \\equiv 0 \\pmod{n}$").scale(0.8)
        step4_formula.next_to(step4_title, DOWN, buff=0.5)
        self.play(Write(step4_formula))
        self.wait(1)
        
        step4_calculation = Tex("$\\left(3^{1633} - 1\\right)\\left(3^{1633} + 1\\right)\\left(3^{3266} + 1\\right) \\cdots \\left(3^{52256} + 1\\right) \\mod 104513 = 0$").scale(0.8)
        step4_calculation.next_to(step4_formula, DOWN, buff=0.5)
        self.play(Write(step4_calculation))
        self.wait(1)
        
        step4_conclusion = Tex("\\textbf{Since } $3^{32*1633} \\equiv 88958 \\equiv -1 \\mod 104513$, $104513$ is probably prime").scale(0.8)
        step4_conclusion.next_to(step4_calculation, DOWN, buff=0.5)
        self.play(Write(step4_conclusion))
        self.wait(2)
        
        # Clear screen
        self.play(FadeOut(step4_title), FadeOut(step4_formula), FadeOut(step4_calculation), FadeOut(step4_conclusion))

class UsefulnessScene(Scene):
    def construct(self):
        # Initial title centered
        title = Tex("Why is Miller-Rabin Test Useful?").scale(1.2)
        title.move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.wait(0.5)

        # Cryptography section
        crypto_title = Tex("1. Cryptography").scale(1.2)
        crypto_title.move_to(ORIGIN)
        self.play(Write(crypto_title))
        self.wait(1)
        self.play(FadeOut(crypto_title))
        self.wait(0.5)

        crypto_points = VGroup(
            Tex("- Used in RSA, Diffie-Hellman and ElGamal key generation"),
            Tex("- Essential for secure communication")
        ).arrange(DOWN, aligned_edge=LEFT)
        crypto_points.scale(0.8)
        crypto_points.move_to(ORIGIN)
        self.play(Write(crypto_points))
        self.wait(2)
        self.play(FadeOut(crypto_points))
        self.wait(0.5)

        # Efficiency section
        efficiency_title = Tex("2. Efficiency").scale(1.2)
        efficiency_title.move_to(ORIGIN)
        self.play(Write(efficiency_title))
        self.wait(1)
        self.play(FadeOut(efficiency_title))
        self.wait(0.5)

        efficiency_points = VGroup(
            Tex("- Much faster than trial division or factoring"),
            Tex("- Can test very large numbers")
        ).arrange(DOWN, aligned_edge=LEFT)
        efficiency_points.scale(0.8)
        efficiency_points.move_to(ORIGIN)
        self.play(Write(efficiency_points))
        self.wait(2)
        self.play(FadeOut(efficiency_points))
        self.wait(0.5)

        # Practicality section
        practicality_title = Tex("3. Practicality").scale(1.2)
        practicality_title.move_to(ORIGIN)
        self.play(Write(practicality_title))
        self.wait(1)
        self.play(FadeOut(practicality_title))
        self.wait(0.5)

        practicality_points = VGroup(
            Tex("- Easy to implement"),
            Tex("- Low probability of error"),
            Tex("- Used in many programming libraries, like SymPy in Python or OpenSSL in C")
        ).arrange(DOWN, aligned_edge=LEFT)
        practicality_points.scale(0.8)
        practicality_points.move_to(ORIGIN)
        self.play(Write(practicality_points))
        self.wait(3)
        self.play(FadeOut(practicality_points))

class EfficiencyScene(Scene):
    def construct(self):
        # Initial title centered
        title = Tex("Efficiency").scale(1.5)
        title.move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.wait(0.5)

        # Time complexity section
        complexity_title = Tex("Time Complexity").scale(1.2)
        complexity_title.move_to(ORIGIN)
        self.play(Write(complexity_title))
        self.wait(1)
        self.play(FadeOut(complexity_title))
        self.wait(0.5)

        complexity = VGroup(
            Tex("$O(k \\log^3 n)$").scale(1.5),  # Made larger
            Tex("where:").scale(1.2),
            Tex("- $k$ is the number of tests").scale(1.2),
            Tex("- $n$ is the number being tested").scale(1.2)
        ).arrange(DOWN, center=True)  # Center aligned
        complexity.move_to(ORIGIN)
        self.play(Write(complexity))
        self.wait(2)
        self.play(FadeOut(complexity))
        self.wait(0.5)

        # Error probability section
        error_title = Tex("Error Probability").scale(1.2)
        error_title.move_to(ORIGIN)
        self.play(Write(error_title))
        self.wait(1)
        self.play(FadeOut(error_title))
        self.wait(0.5)

        # Create axes for the graph - made larger
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.1],
            axis_config={"include_numbers": True},
            x_length=7,  # Increased from 5
            y_length=5,  # Increased from 3
        )
        axes.to_edge(RIGHT, buff=1)

        # Create the error probability curve
        def error_prob(x):
            return 4**(-x)

        curve = axes.plot(error_prob, x_range=[0, 10], color=BLUE)
        curve_label = axes.get_graph_label(curve, label='4^{-k}')
        curve_label.shift(RIGHT * 0.4)  # Move label to the right

        # Text on the left side - smaller and left aligned
        error_text = VGroup(
            Tex("For $k$ tests:").scale(0.8),
            Tex("$\\text{Error} \\leq 4^{-k}$").scale(0.8),
            Tex("Example:").scale(0.8),
            Tex("With $k=10$ tests:").scale(0.8),
            Tex("$\\text{Error} \\leq 4^{-10} \\approx 0.000001$").scale(0.8)
        ).arrange(DOWN, aligned_edge=LEFT)  # Left aligned
        error_text.to_edge(LEFT, buff=1)

        # Animate the scene
        self.play(Write(error_text))
        self.play(Create(axes), Create(curve), Write(curve_label))
        
        # Add dots for k=1 to k=10
        dots = VGroup()
        for k in range(1, 11):
            dot = Dot(axes.c2p(k, error_prob(k)), color=RED)
            dots.add(dot)
            self.play(Create(dot), run_time=0.2)
            self.wait(0.1)

        self.wait(2)
        
        # Clear everything
        self.play(
            FadeOut(error_text),
            FadeOut(axes),
            FadeOut(curve),
            FadeOut(curve_label),
            FadeOut(dots)
        )

def main():
    # Create a list of all scenes in order
    scenes = [
        TitleScene,
        WhatItDoesScene,
        BackgroundScene,
        CarmichaelAndEuclidScene,
        HowItWorksScene,
        ExamplesScene,
        UsefulnessScene,
        EfficiencyScene
    ]
    
    # Run each scene
    for scene in scenes:
        scene().render()

if __name__ == "__main__":
    main()


