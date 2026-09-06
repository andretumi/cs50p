from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.shirt()

    @classmethod
    def get(cls):
        name_input = input("Name: ").strip()
        return cls(name_input)

    def shirt(self):
        # Creating pdf page
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)
        # Writing Title "CS50 Shirtificate"
        pdf.set_font("Helvetica", size=50)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        # Adding shirt image
        pdf.image("shirtificate.png", 5, 80, 200)
        # Writing on shirt "NAME took CS50"
        pdf.set_font("Helvetica", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 180, text=f"{self.name} took CS50", align="C")
        # Generating pdf file
        pdf.output("shirtificate.pdf")


def main():
    Shirtificate.get()


if __name__ == "__main__":
    main()
