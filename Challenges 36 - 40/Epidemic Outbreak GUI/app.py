import random
import math
import tkinter
import time

# Classes

class Simulation():
    def __init__(self):
        # Start in day 1
        self.day_number = 1
        print("In order to simulate an epidemic outbreak, we must know the population size.")
        # Population size
        self.population_size = int(input("---Enter the population size: "))
        
        # We want a perfect square
        root = math.sqrt(self.population_size)
        if int(root + 0.5)**2 != self.population_size:
            root = round(root)
            self.grid_size = int(root)
            self.population_size = self.grid_size**2
            print(f"Rounding population size to {self.population_size} for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))
        # Population initially infected   
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = int(input("---Enter the percentage (0-100) of the population initially infected: "))
        self.infection_percent = self.infection_percent / 100 
        # Probability of infection
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = int(input("---Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_probability = self.infection_probability / 100
        # Infection duration
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("---Enter the duration (in days) of the infection: "))
        # Mortality Rate
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = int(input("---Enter the mortality rate (0-100) of the infection: "))
        print("\nWe must know how long to run the simulation")
        self.sim_days = int(input("---Enter the number of days to simulate: "))

class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self,simulation):
        infection_chance = random.randint(0,100)
        if infection_chance < simulation.infection_probability:
            self.is_infected = True
    
    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self,simulation):
        if self.is_dead == False:
            if self.is_infected:
                self.days_infected += 1
                death_chance = random.randint(0,100)
                if death_chance < simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()

class Population():
    def __init__(self,simulation):
        # We create the list based on the population_size the user submit
        self.population = []
        for i in range(simulation.grid_size):
            row = []
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self,simulation):
        # We start with this many infected
        infected_count = int(round(simulation.population_size * simulation.infection_percent))
        infections = 0
        while infections < infected_count:
            x = random.randint(0,simulation.grid_size - 1)
            y = random.randint(0,simulation.grid_size - 1)
            if self.population[x][y].is_infected == False:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self,simulation):
        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if self.population[i][j].is_dead == False:
                    if i == 0:  # First row
                        if j == 0: # First column
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected: 
                                self.population[i][j].infect(simulation) 
                        elif j == simulation.grid_size - 1: # Last column
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                        else: #Any other column
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    elif i == simulation.grid_size - 1: # Last row
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                             if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    else: # Every other row
                        if j == 0:
                             if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected: 
                                self.population[i][j].infect(simulation) 
                        elif j == simulation.grid_size - 1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected: 
                                self.population[i][j].infect(simulation) 
                        else:
                            if self.population[i][j+1].is_infected or self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected: 
                                self.population[i][j].infect(simulation) 
    
    def update(self,simulation):
        # Update day 
        simulation.day_number += 1 
        # Update each person in the population
        for row in self.population:
            for person in row:
                person.update(simulation)
    
    def display_statistics(self,simulation):
        total_infected_count = 0
        total_death_count = 0
        # Update statistics
        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count += 1
                    if person.is_dead:
                        total_death_count += 1
        # Percentage
        infected_percent = total_infected_count * 100 / simulation.population_size
        infected_percent = round(infected_percent,4)
        death_percent = total_death_count * 100 / simulation.population_size
        death_percent = round(death_percent,4)
        # Summary
        print("\n----- SUMMARY -----")
        print(f"Day {simulation.day_number}")
        print(f"Population infected: {infected_percent}%")
        print(f"Population deceased: {death_percent}%")
        print(f"Total infected: {total_infected_count}")
        print(f"Total deaths: {total_death_count}")

# Function

def graphics(simulation,population,canvas):
    
    square_dimension = 600 // simulation.grid_size
    for i in range(simulation.grid_size):
        y = i * square_dimension    
        for j in range(simulation.grid_size):
            x = j * square_dimension
            # Person is dead
            if population.population[i][j].is_dead:
                canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension,fill="red")
            # Person is alive
            else:
                if population.population[i][j].is_infected: # Infected
                    canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension,fill="yellow")
                else: # Healthy
                    canvas.create_rectangle(x,y,x+square_dimension,y+square_dimension,fill="green")

# Main Code

simulation = Simulation()

# Window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Tkinter window
sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")

# Canvas
sim_canvas = tkinter.Canvas(sim_window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg="lightblue")
sim_canvas.pack(side=tkinter.LEFT)

# Population
population = Population(simulation)
population.initial_infection(simulation)
population.display_statistics(simulation)
input("Press 'Enter' to begin simulation. ")

# Outbreak
for i in range(1,simulation.sim_days):
    population.spread_infection(simulation)
    population.update(simulation)
    population.display_statistics(simulation)
    graphics(simulation,population,sim_canvas)
    # Update the tkinter window
    sim_window.update()
    # We are not currently in the last day
    if i != simulation.sim_days - 1:
        sim_canvas.delete("all")
    time.sleep(0.1)
        