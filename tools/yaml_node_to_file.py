import yaml

from argparse import ArgumentParser

def init_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "yaml_file"
    )
    parser.add_argument(
        "node"
    )
    parser.add_argument(
        "--mode",
        default='normal'
    )
    parser.add_argument(
        "--dump_path",
        default=""
    )
    return parser.parse_args()

def normalise_file_name(name: str) -> str:
    return name.lower().replace(" ", "_")

def main(args: list[str]):
    dump_path = str(args.yaml_file).rstrip(".yaml").replace("views", "cards")

    with open(args.yaml_file) as source_file:
        tree = yaml.safe_load(source_file)

        if args.mode == 'debug': print(tree)

        if args.node not in tree:
            print("Node not in file")
            exit(1)
        else:
            for item in tree[args.node]:
                name = f"{dump_path}/{normalise_file_name(item['title'])}.yaml"

                if args.mode == 'debug':
                    print(name, yaml.dump([item]))
                else:
                    with open(name, "w") as w:
                        yaml.dump([item], w)


if __name__ == "__main__":
    args = init_parser()
    main(args=args)
