description = '''
I please need a golf analysis software program produced to accurately determine a rotation point location along the length of a golf club before a swing even begins. During the period, golfers commonly move a club in a manner that creates a rotation point along the length of the club. In essence it divides the length of the club into two sections. The point location can vary significantly from golfer to golfer even for the same club and is a crucial measurement that needs to be found.

Videos recorded using standard 2D cameras are all that are fundamentally needed and will be utilized for this application version, so appropriate video tracking will be needed. While perhaps a bit less demanding overall than more advanced 3D tracking, club movements during the period can nevertheless be more difficult to track than when actually swinging.

Club movements can range from being quicker and/or more abrupt than might first thought, to so small and/or subtle that they are barely noticeable unless specifically looking for them. Being able to accurately track such club movements is important. It is currently planned to have tracking markers (such as tapes or dots) placed on clubs used in recordings. That will hopefully aid in more accurate tracking, as well as help to more accurately determine certain club dimensions toward determining the needed solution(s).

Attempts have been partly successful previously. One was done using R programming, which had very good tracking accuracy using a color tracking method, and some nice visual graphics. But among other issues, it was far too slow to really be usable, even when tracking just a very small number of video frames/times (expected to be the case in many instances). I think Python was used in a couple of other attempts. But while tracking speed was much better, one had worthless tracking accuracy, and another lacked multiple elements that prevented determining any solution(s).

Additional documentation more extensively details the good and bad of previous attempts for reference (including past code), along with elements or features needed in order to achieve application success. After accurate tracking is successful, the needed solution(s) can be accurately determined. While not especially complex mathematically, some details are involved largely because some overall club movement also commonly occurs during the period. And such movements in essence need to be filtered out to arrive at the needed solution(s). Steps to arrive at the needed solution(s) are also described in the additional documentation.

Because overall application success has not yet been accomplished, I have still not been able to positively prove certain things yet. In that regard I am still somewhat at a prototyping stage. So I am next in need of a basic version of the application that can at least function properly, yet be as efficient as possible from time and cost standpoints. I would basically be working with and testing on my desktop. If successful and if it matters toward choosing an appropriate programming language(s) at this time, subsequent versions might potentially be desktop, web, and/or phone types.

There is no set budget, but I will spend little more on any further attempts unless and until remaining unproven elements are better proven first. I can then take things from there. Despite being a long-struggling project, various IP rights are still in play for this application. So an NDA will likely be required before being able to release and/or discuss the more detailed documentation.

I will consider project or hourly rate proposals, though I cannot really consider completely open-ended hourly rates. For any hourly rate proposals, a reliable quote of hours needed would be required before I would be able to commit. Please feel free to send any questions or comments my way, as I could have easily missed one or more even very basic items that might be needed for your consideration. Thank you very much.
'''
api_key = "sk-proj-4dtgAwOjx36XzZWog9rET3BlbkFJadmSKWvqeTAZMrKzOjy1"
client = ""
if api_key is not None:
    from openai import OpenAI

client = OpenAI(api_key=api_key)
prompt = f"create a proposal for the job descrtiption and format that in html for bullets  "
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": prompt}],
)
objective = response.choices[0].message.content
print(objective)