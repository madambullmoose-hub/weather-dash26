from nicegui import ui
import random

# THE LOCKED LAYOUT (FLEXBOX)
with ui.left_drawer(value=True).style('background-color: #E6B94E; padding: 40px;'):
    ui.label('AI COPILOT').classes('text-4xl font-black italic')
    ui.label('Risk analysis active.').classes('mt-2 text-sm')
    with ui.column().classes('mt-auto pb-10'):
        ui.label('SHORT NOW!').classes('text-5xl font-black leading-none')

with ui.column().classes('w-full bg-black min-h-screen p-8 text-white'):
    ui.label('HIGH TEMP TRADER').classes('text-center text-5xl text-[#99FF00] font-black w-full')
    
    # STATION ROW
    with ui.row().classes('w-full justify-center mt-6 gap-2'):
        for s in ["KNYC", "KMIA", "KPHL", "KMDW"]:
            ui.button(s).props('outline color=white')

    # DATA SECTION (PREVENTS OVERLAPPING)
    with ui.row().classes('w-full mt-10 items-start'):
        with ui.card().classes('bg-white text-black p-6 flex-grow'):
            ui.label('Philadelphia Highest Temp?').classes('text-xl font-bold')
            # Preserving numbers after the decimal point as requested
            ui.label('51.00° or below: 1.01x (98.00%)').classes('text-lg border-b w-full py-2')
            ui.label('52.00° to 53.00°: 23.40x (4.00%)').classes('text-lg w-full py-2')

        with ui.column().classes('ml-10'):
            ui.label('PHILADELPHIA (KPHI)').classes('text-sm opacity-70')
            ui.label('CURRENT TEMP:').classes('mt-4')
            # NiceGUI labels update without refreshing the whole page
            temp_display = ui.label('47.60').classes('text-7xl text-red-500 font-mono font-bold')

# Bypassing the local Mac install by running on the cloud port
ui.run(host='0.0.0.0', port=7860, title='High Temp Trader')
