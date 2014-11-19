from Tkinter import *
import random, sys, time

root = Tk()
root.wm_title("Flappy Bird")
width = 500 
height = 500
canvas = Canvas(root, width = width, height = height, bg = "light blue")
canvas.pack()
pipe_speed = 5.0
player_jump = False
score = 0
player_pos = [20, height / 2, 40, height / 2 + 20]
canvas.create_rectangle(player_pos, fill = "blue", tag = "player")
score_id = canvas.create_text(40, 20)
jump_count = 0
player_speed = 3
canvas.insert(score_id, 0, "Score: " + str(score))
        
def jump_animate():
    global player_pos, player_jump, jump_count, player_speed
    canvas.move("player", 0, -player_speed)
    player_pos[1] -= player_speed 
    player_pos[3] -= player_speed 
    player_speed -= 0.09
    jump_count += 3
    if jump_count >= 100:
        player_jump = False
    if player_jump:
        canvas.after(10, jump_animate)
    
def game_over():
    global pipe_speed, pipe_bottom, pipe_pos
    canvas.delete("rect")
    canvas.delete("player")
    game_overid = canvas.create_text(width / 2, height / 2)
    canvas.insert(game_overid, 0, "Game Over! Your score was " + str(score) + " pipes!")
    pipe_speed = 0
    pipe_pos = [width + 50, 0, width + 100, height]
    pipe_bottom = pipe_pos

def draw_pipe():
    global score
    canvas.create_rectangle(list(pipe_pos), fill = "green", tag = "rect", outline = "green")
    canvas.create_rectangle(list(pipe_bottom), fill = "green", tag = "rect", outline = "green")
    if pipe_pos[2] <= -5:
        score += 1
        canvas.itemconfig(score_id, text = "Score: " + str(score)) 
        generate_pipe()
    canvas.after(1000, draw_pipe)
    
def generate_pipe():
    global pipe_pos, pipe_bottom
    pipe_hole = random.randrange(150, height - 150)
    pipe_pos = [width - 50, 0, width, pipe_hole]
    pipe_bottom = [width - 50, pipe_pos[3] + 135, width, height]
    draw_pipe()

def check_hit():
    global coun
    if player_pos[0] <= pipe_pos[2] and player_pos[2] >= pipe_pos[0] and player_pos[1] <= pipe_pos[3] and player_pos[3] >= pipe_pos[1]:
        game_over()
    if player_pos[0] <= pipe_bottom[2] and player_pos[2] >= pipe_bottom[0] and player_pos[3] <= pipe_bottom[3] and player_pos[3] >= pipe_bottom[1]:
        game_over()
    if player_pos[3] >= height + 5:
        game_over()
    canvas.after(10, check_hit)

def move_items():
    global player_pos, player_speed
    canvas.move("rect", -pipe_speed, 0)
    pipe_bottom[0] -= pipe_speed
    pipe_bottom[2] -= pipe_speed
    pipe_pos[0] -= pipe_speed
    pipe_pos[2] -= pipe_speed
    if player_jump == False:
        canvas.move("player", 0, player_speed)
        player_pos[1] += player_speed
        player_pos[3] += player_speed
        player_speed += 0.15
    canvas.after(10, move_items)

def jump(press):
    global player_jump, jump_count, player_speed
    player_jump = True
    player_speed = 3
    jump_count = 0
    jump_animate()

canvas.bind("<Button-1>", jump)
generate_pipe()
move_items()
check_hit()
root.mainloop()
