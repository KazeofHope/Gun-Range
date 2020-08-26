import json

class Testing_Ground:
    def __init__(self):
        self.prev_data = {
"Shooting Range Data" :
{
  "Pistol" :
  {
    "Classic" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Shorty" : {
      "Data" : {
        "Easy" : [

        ], "Medium" : [

        ], "Hard" : [

        ]
      }
    },
    "Frenzy" : {
      "Data" : {
        "Easy" : [

      ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Ghost" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Sheriff" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  },
  "SMG" : {
    "Stinger" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Spectre" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  },
  "Shotgun" : {
    "Bucky" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Judge" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  },
  "AR" : {
    "Bulldog" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Guardian" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Phantom" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Vandel" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  },
  "Sniper" : {
    "Marshal" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Operator" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  },
  "LMG" : {
    "Ares" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    },
    "Odin" : {
      "Data" : {
        "Easy" : [

        ],
        "Medium" : [

        ],
        "Hard" : [

        ]
      }
    }
  }
}
}
        self.associated_filepath = None
        self.gun_types = list(self.prev_data.get(list((self.prev_data.keys()))[0]).keys())
        self.gun_names = []
        self.current_gun = None
        self.current_training_mode = None
        self.new_data = []

        for i in self.gun_types:
            self.gun_names.extend(list(self.prev_data.get(list(self.prev_data.keys())[0]).get(i).keys()))

    def download_data(self, filepath): # downloads list from json file
        self.associated_filepath = filepath
        with open("{}".format(self.associated_filepath)) as f:
            self.prev_data = json.load(f)

    def exporting_data(self, filepath):
        for i in self.prev_data.get("Shooting Range Data"):
            if self.current_gun in (self.prev_data.get("Shooting Range Data" ).get(i)):
                # self.prev_data.get("Shooting Range Data" ).get(i).get(self.current_gun).get("Data").update({self.current_training_mode :
                t = self.prev_data.get("Shooting Range Data" ).get(i).get(self.current_gun).get("Data").get(self.current_training_mode).extend(self.new_data)
                print(t)

        new_data = self.prev_data # updated data

        with open(f'{filepath}', 'w') as json_file:
            print(new_data)
            json.dump(new_data, json_file)

    def practice_session_start(self):
        def find_average_scores(current_gun):
            averages = []
            for i in (self.prev_data.get(list(self.prev_data.keys())[0])):
                if current_gun in (self.prev_data.get(list(self.prev_data.keys())[0]).get(i)):
                    for j in list(self.prev_data.get(list(self.prev_data.keys())[0]).get(i).get(current_gun).get("Data").keys()):
                        if len(self.prev_data.get(list(self.prev_data.keys())[0]).get(i).get(current_gun).get("Data").get(j)) == 0:
                            averages.append("No Data")
                        else:
                            averages.append(sum(self.prev_data.get(list(self.prev_data.keys())[0]).get(i).get(current_gun).get("Data").get(j))/len(self.prev_data.get(list(self.prev_data.keys())[0]).get(i).get(current_gun).get("Data").get(j)))
            return averages

        print(
            "Welcome to your personal Valorant Shooting Range Data Recorder\n"
            "Which gun would you like to practice on in this session?\n"
            f"{self.gun_names}"
        )
        while True:
            self.current_gun = input()
            if self.current_gun in self.gun_names:
                break
            else:
                print("Improper Input")

        avg = find_average_scores(self.current_gun)

        print(
            f"Training with {self.current_gun}"
            f"\tYour Average Scores by difficulty\n"
            f"Easy || Medium || Hard\n"
            f"{avg}"
        )

        print(
            "Which mode are you going to train in?\n"
            "Easy || Medium || Hard"
        )
        while True:
            self.current_training_mode = input()
            if self.current_training_mode == "Easy" or "Medium" or "Hard":
                break
            else:
                print("Improper Input")

        i = 0
        while True:
            if i == 0:
                print(f"Training Round {i} - Warm up")
                self.warmup_score = input("Input warm up score: ")

            elif i > 0:
                print(f"Training Round {i}")
                while True:
                    n = int(input("Input Score "))
                    if n > -1 and n < 31:
                        break
                    else:
                        print("Improper Input")
                self.new_data.append(n)

            i = i + 1

            while True:
                user_input = input("Would you like to continue? (Y/N) ")
                if user_input == "Y" or user_input == "N":
                    break
                else:
                    "Improper Input"

            if user_input == "N":
                break



        print(
            f"Results of Training Session\n"
            f"# of Rounds: {i}\n"
            f"Scores: {self.new_data}\n"
            f"\n"
            f"Would you like to export this data to your dataset? (Y/N) \n"
        )
        while True:
            user_input = input()
            if user_input == "Y" or user_input == "N":
                break
            else:
                "Improper Input"

        if user_input == "Y":
            self.exporting_data(self.associated_filepath)
        else:
            return f"New Scores for {self.current_gun}: {self.new_data}"




if __name__ == "__main__":

    filepath = r"C:\Users\vsbas\PycharmProjects\ECE homework 241 11\Stupid Projects\gun_skill_data.json"
    training_session = Testing_Ground()
    training_session.download_data(filepath)
    training_session.practice_session_start()