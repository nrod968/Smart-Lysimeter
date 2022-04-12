from tkinter import *
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_popup(root, message, title):
    top = Toplevel(root)
    top.geometry("750x270")
    top.title(title)
    Label(top, text= message, font=('Mistral 18 bold')).place(x=150,y=80)

def create_filleted_rectangle(canvas: Canvas, x0, y0, x1, y1, cornerRadius, fill='', outline='', text="", font=None, tag=""):
        points = [
            x0,(y0 + cornerRadius), (x0 + cornerRadius),(y0 + cornerRadius), (x0 + cornerRadius),y0,
            (x1 - cornerRadius),y0, (x1 - cornerRadius),(y0 + cornerRadius), x1,(y0 + cornerRadius),
            x1,(y1 - cornerRadius), (x1 - cornerRadius),(y1 - cornerRadius), (x1 - cornerRadius),y1,
            (x0 + cornerRadius),y1, (x0 + cornerRadius),(y1 - cornerRadius), x0,(y1 - cornerRadius)
        ]
        canvas.create_polygon(points, fill=fill, outline='', tag=tag)

        canvas.create_arc(
            x0, y0, (x0 + 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline='', start=90, extent=90, tag=tag
        )
        canvas.create_arc(
            x1, y0, (x1 - 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline='', start=0, extent=90, tag=tag
        )
        canvas.create_arc(
            x1, y1, (x1 - 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline='', start=270, extent=90, tag=tag
        )
        canvas.create_arc(
            x0, y1, (x0 + 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline='', start=180, extent=90, tag=tag
        )

        canvas.create_arc(
            x0, y0, (x0 + 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline=outline, start=90, extent=90, style=ARC, tag=tag
        )
        canvas.create_arc(
            x1, y0, (x1 - 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline=outline, start=0, extent=90, style=ARC, tag=tag
        )
        canvas.create_arc(
            x1, y1, (x1 - 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline=outline, start=270, extent=90, style=ARC, tag=tag
        )
        canvas.create_arc(
            x0, y1, (x0 + 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline=outline, start=180, extent=90, style=ARC, tag=tag
        )

        canvas.create_line((x0 + cornerRadius),y0, (x1 - cornerRadius),y0, fill=outline, tag=tag)
        canvas.create_line(x1,(y0 + cornerRadius), x1,(y1 - cornerRadius), fill=outline, tag=tag)
        canvas.create_line((x1 - cornerRadius),y1, (x0 + cornerRadius) - 2,y1, fill=outline, tag=tag)
        canvas.create_line(x0,(y1 - cornerRadius), x0,(y0 + cornerRadius) - 2, fill=outline, tag=tag)

        if (text != ""):
            canvas.create_text((x0 + x1) / 2.0, (y0 + y1) / 2.0, anchor="center", text=text, fill="#000000", font=font, tag=tag)