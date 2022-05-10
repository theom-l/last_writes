import openai
import requests

# TO DO Variables collected from USB
device_name = "fall 2012 classes"
device_created = "Jan 14, 2010"
last_modified = "June 10, 2016"
# oldest_file = "September 29, 2012"
# device_size = "15.98 GB"
# directories = ["Urban Design Lab", "old", "drafts", "rhino model files", "lasercut files proj 3", "export 1", "export 2", "final models", "exhibit photos"]
# file_types = "48 .3dm files"
# IMG - generate from data

obit = "initialize"


class GPT3_Api:
    def __init__(self) -> None:
        self.gpt3 = ""

    def gpt3_request(self):
        global device_name
        global device_created
        global last_modified
        obit = "initialize"
        openai.api_key = "API-KEY"
        # initialize prompt
        prompt = "Say this is a test."
        # Request GPT3 with text from transcription
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt="Using the following information:\n\nToday's date\nDevice name: fall 2012 classes\nDevice manufacture date: Jan 14, 2010\nDevice manufacturer: Seagate\nFirst time a file was created: September 29, 2012\nLast time a file was modified: June 10, 2016\nDevice total size: 15.98 GB\nDevice space used: 9.11 GB\nDevice free space: 6.86 GB\nDirectories: \"Urban Design Lab\", \"old\", \"drafts\", \"rhino model files\", \"lasercut files proj 3\", \"export 1\", \"export 2\", \"final models\", \"exhibit photos\"\nContains file types: .3dm, .ai, .psd, .pdf, .dwg, .png, .jpg, .tiff, .stl\nOldest file name: resume_new.pdf\nNewest file name: building_wsite_finalFinal6.3dm\n\nWrite an 250 word obituary for a USB memory stick that will be recycled.",
                temperature=.83,
                max_tokens=2030,
                top_p=1,
                frequency_penalty=0.08,
                presence_penalty=0.08
            )
            answer = response
        except requests.RequestException:
            print("ERROR: Not able to contact OpenAI API")

        # parsing JSON from GPT3
        obit = (device_name + "\n" + device_created + " - " +
                last_modified + "\n\n" + answer['choices'][0]['text'] + "\n\n")

        return obit
