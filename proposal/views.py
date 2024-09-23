from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from projects.models import Project, TechStack
from .models import Job
from .serializers import JobSerializer


class JobProcessingAPIView(APIView):

    def post(self, request):
        argon = ''' We are ArgonTeq (part of Ozi Group) and we create first-rate and superior websites and applications. To date, we have delivered 350+ websites and mobile apps for our global clients which have given us an immense feeling of happiness, and boast of developing some of the big brand websites and applications with millions of views.
In this proposal, you'll see information about ArgonTeq, our services, project description, development process, pricing, terms, and conditions.
We look forward to talking with you.
Sincerely, ArgonTeq 
For over 7 years, we've been developing new technology and helping Enterprises, Governments, NGOs and Startups, globally from all sizes to grow and achieve their goals in the form of users, subscription and revenue. Our mission is to provide companies with cutting-edge services that will enable you to achieve your goals via digital means.
We strongly believe that our proficient technical practices fetch promising results for you. No matter where you start from, we ensure that where you reach must be noticeable and appreciable.
At ArgonTeq, we believe in a thorough approach that provides our clients with as much engagement as they request. While our entire team will be developing your web/app, we will assign a project lead who will be your main point of contact.
We normally need 2-20 weeks to finish the Application completely, depending upon the complexity of the requirement. We send feedback to our client for every successful step we make. We assure our clients that we kept them updated with the project.
1.	Zoom Meeting and formally offering the proposal.
2.	Acknowledgment and signing of contracts. 
3.	Proceed with building the app UI screens.
4.	Create the front-end technology of the app. 
5.	Improve visual UI design. 
6.	Programming the backend technology of the app. 
7.	Perform UX (User Experience) QA Testing. 
8.	Perform further testing with the client. 9. Go Live for public release
Warranty of Services
ArgonTeq assures that the services offered will be in excellent and first-rate quality. For changes in the way of how we render our service, please notify the company. If you are not satisfied with our work, kindly let us know so that we can further assist you.
Payment
Payment would be divided into 4 parts on a 25%-25%-25%-25% basis i.e. 25%% advance with this proposal, 25% after the first milestone is completed, 25% after the second milestone is completed, 25% after 3rd Milestone when UAT Start.
IPR
ArgonTeq acknowledges that all intellectual property rights in the work product, including but not limited to software, documentation, and other materials created by the agency, will be owned by the client. ArgonTeq hereby assigns and transfers all intellectual property rights in the work product to the client.
Amendments
This Proposal can only be changed or modified by the company ArgonTeq. A new proposal will be made if the clients wish to change the content of the document.

'''
        api_key = "sk-proj-4dtgAwOjx36XzZWog9rET3BlbkFJadmSKWvqeTAZMrKzOjy1"
        client = ""
        if api_key is not None:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
        # Deserialize the incoming Job data
        job_serializer = JobSerializer(data=request.data)

        if job_serializer.is_valid():
            # Save the Job object
            job = job_serializer.save()

            # Extract tech stack from job description (assuming tech stack is provided)

            prompt = f"your task is that you will be given a client technical requiremnsts and you have to get the tech stacks like python react vue dotnet django flask fastapi  etc seprated by commas {job.description}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=10,
            )
            tech_stacks = response.choices[0].message.content
            print(tech_stacks.split(','))
            tech_stack_names = request.data.get('tech_stack', tech_stacks)
            tech_stack_objs = TechStack.objects.filter(name__in=tech_stack_names)

            # Find Projects with the same tech stack
            matching_projects = Project.objects.filter(tech_stack__in=tech_stack_objs).distinct()

            projects_description = "and here are some relevant project done "
            for project in matching_projects:
                projects_description = projects_description + project.description + ' '

            prompt = f"Your task is to write a cover-letter we are a agency named Argon here is some information about company {argon} for the given job description {job.description} and the client name is {job.client} mention that i have worked with all the things mentioned important point is to note make sure to add objective, scope, budget, deadline, and milestone here are some relevant projects which you can add {projects_description} in detail the proposal should be at least 3-4 pages long explain the milestones time or those milestones and mention some projects similar to this  add the terms for argon as decscibed above   format the response in such way which i can directly use in rich text editor for formatiing you can provide me a html response  every thing should be well formated like headings bullet points list each and ervy thing in a html format which can be used in rich text editor dont include [Doctype,styling,<html tag> <body> ] just the html code h tags for headings line breaks listing numbering  make the html formating beautiful and well organized so that it should look like a professional proposal "
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}],
            )
            proposal_response = response.choices[0].message.content
            print(proposal_response)
            return Response({
                'data': proposal_response,

            }, status=status.HTTP_200_OK)

        return Response(job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
