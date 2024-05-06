from utils.generator import SceneGenerator
import fire


def main():
    print("Coming up with candidate scenes ....")
    prompt = "Create a scene with ten orange circle, and arrange four blue rectangles."
    SceneGenerator().run(prompt)

if __name__ == "__main__":
    fire.Fire(main)