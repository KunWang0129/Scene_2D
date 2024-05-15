from utils.generator import SceneGenerator

print("Coming up with candidate scenes ....")
SceneGenerator().run("""Create a scene with with the following drawing steps: 
1. A rectangle is placed in the center of the scene (car body).
2. Two smaller rectangles are placed on the top of the car body (windows).
3. Two circles are placed on the bottom of the car body (wheels).
4. A smaller rectangle is placed at the front of the car body (front bumper).
5. Another smaller rectangle is placed at the back of the car body (rear bumper).""")