from flask import Flask, request, redirect
from dataclasses import dataclass
from dice import zig_roll as roll


app = Flask(__name__)

@dataclass
class Entity:
    name: str
    hp: int
    ac: int
    hit: int
    dmg: int
    initiative: int

storm = Entity("Storm", 100, 19, 8, 10, 5)
gobw = Entity("Goblin Warrior", 50, 15, 8, 7, 3)
goba = Entity("Goblin Archer", 40, 13, 8, 4, 3)
gobm = Entity("Goblin Mage", 30, 14, 8, 4, 3)
goba2 = Entity("Goblin Archer", 35, 14, 8, 4, 3)


combat_log = []
turn = 0
combatants = [storm, gobw, goba, gobm, goba2]

for c in combatants:
    c.initiative = roll(1,20) + c.initiative

combatants = sorted(combatants, key=lambda combatant: combatant.initiative, reverse=True)

@app.route('/')
def combat_interface():
    log_content = '\n'.join(combat_log[-4:])
    combatants_initiative = '\n'.join(f"{c.name}: {c.initiative} initiative" for c in combatants)

    return f"""
    <html>
    <head>
        <title>D&D Combat Log</title>
        <style>
            body {{
                font-family: 'Courier New', monospace;
                max-width: 600px;
                margin: 20px;
                padding: 20px;
                background: #f0e6d2;
            }}
            .log-container {{
                border: 3px solid #8b4513;
                max-width: 600px;
                max-height: 200px;
                padding: 20px;
                background: white;
            }}
            form {{
                margin-top: 20px;
            }}
            .button-container {{
                position: absolute;
                display: flex;
                gap: 10px;
                left: 50;
                margin-top: 20px;
            }}
            button {{
                padding: 10px 10px;
                font-size: 10px;
                cursor: pointer;
                top: -100px;
            }}
            .combatants{{
                display: auto;
                position: relative;
                top: -50px;
                right: -300px;
            }}
        </style>
    </head>
    <body>
        <h1>🗡️ D&D Combat Log 🛡️</h1>

        <div class="log-container">
            <h3>Battle Events:</h3>
            <pre>{log_content}</pre>  <!-- Show last 10 entries -->
        </div>

        <form method="POST" action="/handle_action">
            <input type="text" name="action" placeholder="Log a commnet" size="20">
            <button type="submit" name="action_type" value="log">Add to Log</button>
        </form>

        <div class="button-container">
            <form method="POST" action="/handle_action">
                <button type="submit" name="action_type" value="clear">Clear Log</button>
            </form>
            <form method="POST" action="/handle_action">
                <button type="submit" name="action_type" value="storminate">Storminate</button>
            </form>
            <form method="POST" action="/handle_action">
                <button type="submit" name="action_type" value="end_turn">End Turn</button>
            </form>
        </div>

        <div class="combatants">
            <form method="POST" action="/combatants">
            <h3>Initiative Combatants</h3>
            <pre>{combatants_initiative}</pre>
        </div>

    </body>
    </html>
    """

@app.route('/handle_action', methods=['POST'])
def handle_action():
    action_type = request.form.get('action_type')
    if action_type == 'log':
        action = request.form.get('action')
        if action:
            combat_log.append(f"⚔️ {action}")
    elif action_type == 'clear':
        combat_log.clear()
    elif action_type == 'storminate':
        for c in combatants:
            if c.name == "Storm":
                continue
            damage = roll(8,6) if roll(1,20) + 5 < 17 else 0
            c.hp -= damage
            combat_log.append(f"⚡{c.name} takes {damage} from Storm")
    elif action_type == 'end_turn':
        global turn
        turn += 1
        for c in range(1,len(combatants)):
            combatants[c-1], combatants[c] = combatants[c], combatants[c-1]
    return redirect('/')

if __name__ == '__main__':
    app.run()
