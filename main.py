from recomb import TopologicalLens
from populate import Populate
from meander import Meander

def main():
    n = 5
    lens_ids = ["settings", "characters", "worlds"]
    for lens_id in lens_ids:
        # Create a TopologicalLens instance
        topological_lens = TopologicalLens(n, lens_id)
        topological_lens.generate_connections()
        lens_dict = topological_lens.get_edge_ids()

        populator = Populate(lens_dict)
        populated = populator.user_populate_lens_dict()

        meander = Meander(populated)
        md = meander.walk(5)
        print(lens_id)
        print("-----------------------------")
        print(md)
        print("-----------------------------")

if __name__ == "__main__":
    main()
