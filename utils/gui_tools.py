from tkinter import *

def create_filleted_rectangle(canvas, x0, y0, x1, y1, cornerRadius, fill='', outline='', text="", font=None):
        points = [
            x0,(y0 + cornerRadius), (x0 + cornerRadius),(y0 + cornerRadius), (x0 + cornerRadius),y0,
            (x1 - cornerRadius),y0, (x1 - cornerRadius),(y0 + cornerRadius), x1,(y0 + cornerRadius),
            x1,(y1 - cornerRadius), (x1 - cornerRadius),(y1 - cornerRadius), (x1 - cornerRadius),y1,
            (x0 + cornerRadius),y1, (x0 + cornerRadius),(y1 - cornerRadius), x0,(y1 - cornerRadius)
        ]
        canvas.create_polygon(points, fill=fill, outline='')

        canvas.create_arc(
            x0, y0, (x0 + 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline='', start=90, extent=90
        )
        canvas.create_arc(
            x1, y0, (x1 - 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline='', start=0, extent=90
        )
        canvas.create_arc(
            x1, y1, (x1 - 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline='', start=270, extent=90
        )
        canvas.create_arc(
            x0, y1, (x0 + 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline='', start=180, extent=90
        )

        canvas.create_arc(
            x0, y0, (x0 + 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline=outline, start=90, extent=90, style=ARC
        )
        canvas.create_arc(
            x1, y0, (x1 - 2 * cornerRadius), (y0 + 2 * cornerRadius),
            fill=fill, outline=outline, start=0, extent=90, style=ARC
        )
        canvas.create_arc(
            x1, y1, (x1 - 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline=outline, start=270, extent=90, style=ARC
        )
        canvas.create_arc(
            x0, y1, (x0 + 2 * cornerRadius), (y1 - 2 * cornerRadius),
            fill=fill, outline=outline, start=180, extent=90, style=ARC
        )

        canvas.create_line((x0 + cornerRadius),y0, (x1 - cornerRadius),y0, fill=outline)
        canvas.create_line(x1,(y0 + cornerRadius), x1,(y1 - cornerRadius), fill=outline)
        canvas.create_line((x1 - cornerRadius),y1, (x0 + cornerRadius) - 2,y1, fill=outline)
        canvas.create_line(x0,(y1 - cornerRadius), x0,(y0 + cornerRadius) - 2, fill=outline)

        if (text != ""):
            canvas.create_text((x0 + x1) / 2.0, (y0 + y1) / 2.0, anchor="center", text=text, fill="#000000", font=font)