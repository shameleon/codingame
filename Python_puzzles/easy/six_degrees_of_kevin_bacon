import sys

"""
https://www.codingame.com/ide/puzzle/six-degrees-of-kevin-bacon
50% success
"""

class Actor:
    def __init__(self, name):
        self.name = name
        self.movies = set()
        self.played_with = set()
        self.kevin_bacon_index = -1

    def add_movie(self, movie: str, cast: list):
        if self.name in cast:
            self.movies.add(movie)
            for other_actor in cast:
                if other_actor != self.name:
                    self.played_with.add(other_actor)

    def __repr__(self):
        result = f'{self.name}'
        #result += f'\nmovies : {", ".join([x for x in self.movies])}\n'
        #result += f'\nplayed with : {", ".join([x for x in self.played_with])}\n'
        result += f' Kevin Bacon\'s index : {self.kevin_bacon_index}.'
        return result

class DegreesToKevinBacon:
    def __init__(self, data: dict, target_actor: str):
        self.target_actor = target_actor
        self.d = data
        self.actor_names = set()
        for movie, cast in data.items():
            print(f"{movie} :\n{', '.join([x for x in cast])}.\n", file=sys.stderr, flush=True)
            for actor in cast:
                self.actor_names.add(actor)
        self.actors = []
        for actor_name in self.actor_names:
            self.actor_entry(actor_name)
        self.kevin_bacon_indexes()
        for actor in self.actors:
            print(actor, file=sys.stderr, flush=True)

    def actor_entry(self, actor_name):
        actor = Actor(actor_name)
        if actor_name == 'Kevin Bacon':
            actor.kevin_bacon_index = 0
            self.head = actor
        self.actors.append(actor)
        for movie, cast in self.d.items():
            actor.add_movie(movie, cast)

    def get_actor(self, actor_name: str) -> Actor:
        for actor in self.actors:
            if actor_name == actor.name:
                return actor
        return Actor("N/A")

    def names_of_unvisited(self):
        return [actor.name for actor in self.actors if actor.kevin_bacon_index == -1]

    def nb_unvisited(self, actor_names: set) -> int:
        return [self.get_actor(name).kevin_bacon_index for name in actor_names].count(-1)

    def kevin_bacon_indexes(self):
        self.spread_index_to_neighbors(self.head)
        while self.names_of_unvisited():
            for unvisited_name in self.names_of_unvisited():
                unvisited = self.get_actor(unvisited_name)
                actors = [self.get_actor(name) for name in unvisited.played_with]
                kb_indexes = [actor.kevin_bacon_index for actor in actors if actor.kevin_bacon_index >=0]
                if kb_indexes:
                    unvisited.kevin_bacon_index = min(kb_indexes) + 1

    def spread_index_to_neighbors(self, actor: Actor):
        idx = actor.kevin_bacon_index
        print(actor.name, actor.kevin_bacon_index, file=sys.stderr, flush=True)
        for other_name in actor.played_with:
            other = self.get_actor(other_name)
            if other.kevin_bacon_index == -1:
                other.kevin_bacon_index = actor.kevin_bacon_index + 1
            else:
                if other.kevin_bacon_index > idx + 1:
                    other.kevin_bacon_index = idx + 1

    def get_kevin_bacon_index(self, actor_name: str):
        actor = self.get_actor(actor_name)
        if actor.name == "N/A":
            return actor.name
        return str(actor.kevin_bacon_index)


def main():
    actor_name = input()
    print(f'Actor name : {actor_name}\n', file=sys.stderr, flush=True)
    n = int(input())
    data = {}
    for i in range(n):
        movie_cast = input().split(': ')
        data[movie_cast[0]] = movie_cast[1].split(', ')
    degrees = DegreesToKevinBacon(data, actor_name)
    print(degrees.get_kevin_bacon_index(actor_name))

if __name__ =='__main__':
    sys.exit(main())
