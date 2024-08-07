from openpyxl.styles import (
    Font,
    Alignment,
    Border,
    Side,
)

header = Font(name='Calibri', size=11, bold=True)
center = Alignment(horizontal='center', vertical='center', wrap_text=True)
border = Border(
    left=Side(border_style='thin', color='000000'),
    right=Side(border_style='thin', color='000000'),
    top=Side(border_style='thin', color='000000'),
    bottom=Side(border_style='thin', color='000000'),
)