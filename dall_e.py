from openai import OpenAI
client = OpenAI()



def imageGeneration(task_output):
    prompt_results = task_output.result()
    print("## Here is your raw output string")
    print("########################\n")
    print(prompt_results)
    

    response1 = client.images.generate(
    model="dall-e-3",
    prompt=prompt_results[0],
    size="1024x1024",
    quality="standard",
    n=1,
    )

    response2 = client.images.generate(
    model="dall-e-3",
    prompt=prompt_results[1],
    size="1024x1024",
    quality="standard",
    n=1,
    )

    response3 = client.images.generate(
    model="dall-e-3",
    prompt=prompt_results[2],
    size="1024x1024",
    quality="standard",
    n=1,
    )
    images = [response1.data[0].url, response2.data[0].url, response3.data[0].url]
    print("########################\n")
    print("## Three links with Dall-e generated images:")
    print(images)
    return images
