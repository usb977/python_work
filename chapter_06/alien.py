alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

speed_value = alien_0.get('speed','No speed value assigned.')
print(speed_value)