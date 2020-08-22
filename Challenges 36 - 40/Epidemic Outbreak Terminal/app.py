import random

class Simulation():
    def __init__(self):
        self.day_number = 1
        print("In order to simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = int(input("---Enter the percentage (0-100) of the population initially infected: "))
        self.infection_percent = self.infection_percent / 100 # We divide by 100 to transform it into a percentage
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = int(input("---Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_probability = self.infection_probability / 100
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("---Enter the duration (in days) of the infection: "))
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
        for i in range(simulation.population_size):
            person = Person()
            self.population.append(person)
    
    def initial_infection(self,simulation):
        # We start with this many infected
        infected_count = int(round(simulation.population_size * simulation.infection_percent))
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
        # We don't want all infected at the beginning of the list, so we shuffle it    
        random.shuffle(self.population)

    def spread_infection(self,simulation):
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                if i == 0: # This is the first person in the list, so it only has one person next to it 
                    if self.population[i+1].is_infected: # Check if that person is infected
                        self.population[i].infect(simulation) 
                elif i < len(self.population) - 1: # Person that has 2 others next to it
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                elif i == len(self.population) - 1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)
    
    def update(self,simulation):
        # Update day 
        simulation.day_number += 1 
        # Update each person in the population
        for person in self.population:
            person.update(simulation)
    
    def display_statistics(self,simulation):
        total_infected_count = 0
        total_death_count = 0
        # Update statistics
        for person in self.population:
            if person.is_infected:
                total_infected_count += 1
                if person.is_dead:
                    total_death_count += 1
        # Percentage
        infected_percent = total_infected_count * 100 / len(self.population)
        infected_percent = round(infected_percent,4)
        death_percent = total_death_count * 100 / len(self.population)
        death_percent = round(death_percent,4)
        # Summary
        print("\n----- SUMMARY -----")
        print(f"Day {simulation.day_number}")
        print(f"Population infected: {infected_percent}%")
        print(f"Population deceased: {death_percent}%")
        print(f"Total infected: {total_infected_count}")
        print(f"Total deaths: {total_death_count}")

    def graphics(self):
        status = []
        for person in self.population:
            # Person is dead
            if person.is_dead:
                char = "X" # dead
            # Person is alive    
            elif person.is_infected:
                char = "I" # infected
            else:
                char = "O" # healthy
            status.append(char)
        for i in status:
            print(i, end="-")    


# Main code

simulation = Simulation()
population = Population(simulation)

# Initial infection
population.initial_infection(simulation)
population.display_statistics(simulation)
population.graphics()
input("\nPress 'Enter' to begin simulation")

# Outbreak
for i in range(1,simulation.sim_days):
    population.spread_infection(simulation)
    population.update(simulation)
    population.display_statistics(simulation)
    population.graphics()
    if i != simulation.sim_days - 1:
        input("\nPress 'Enter' to advance to the next day. ")

