import json
import numpy as np
import matplotlib.pyplot as plt

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
                self.prev_data.get("Shooting Range Data" ).get(i).get(self.current_gun).get("Data").get(self.current_training_mode).extend(self.new_data)

        new_data = self.prev_data

        with open(f'{filepath}', 'w') as json_file:
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
                    n = int(input("Input Score: "))
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
            print(f"New Scores for {self.current_gun}: {self.new_data}")

    def visualize_all_scores(self):
        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        easy_data = []
        medium_data = []
        hard_data = []
        labels = []

        for i in self.prev_data.get("Shooting Range Data"):
            for j in self.prev_data.get("Shooting Range Data").get(i):
                labels.append(j)
                a = len(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Easy"))
                b = len(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Medium"))
                c = len(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Hard"))
                if a > 0:
                    easy_data.append(sum(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Easy"))/a)
                else:
                    easy_data.append(0)

                if b > 0:
                    medium_data.append(sum(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Medium"))/b)
                else:
                    medium_data.append(0)

                if c > 0:
                    hard_data.append(sum(self.prev_data.get("Shooting Range Data").get(i).get(j).get("Data").get("Hard"))/c)
                else:
                    hard_data.append(0)

        X = np.arange(len(labels))
        width = 0.25

        fig, ax = plt.subplots()
        ax.bar(X - width/2, easy_data, width, label= 'Easy', color= 'g')
        ax.bar(X + width/2, medium_data, width, label= 'Medium', color= 'y')
        ax.bar(X + 3*width/2, hard_data, width, label= 'Hard', color= 'r')

        ax.set_ylabel('Scores')
        ax.set_title('Scores by Gun')
        plt.ylim(0, 30)
        ax.set_xticks(X + width / 2)
        ax.set_xticklabels(labels)
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        ax.legend()

        plt.show()

    def visualize_category(self, category = None):
        labels = []
        easy_data = []
        medium_data = []
        hard_data = []
        sect_data = self.prev_data.get("Shooting Range Data").get(category)
        for i in sect_data:
            labels.append(i)
            if len(sect_data.get(i).get("Data").get("Easy")) > 0:
                easy_data.append(sum(sect_data.get(i).get("Data").get("Easy"))/len(sect_data.get(i).get("Data").get("Easy")))
            else:
                easy_data.append(0)

            if len(sect_data.get(i).get("Data").get("Medium")) > 0:
                medium_data.append(sum(sect_data.get(i).get("Data").get("Medium"))/len(sect_data.get(i).get("Data").get("Medium")))
            else:
                medium_data.append(0)

            if len(sect_data.get(i).get("Data").get("Hard")) > 0:
                hard_data.append(sum(sect_data.get(i).get("Data").get("Hard"))/len(sect_data.get(i).get("Data").get("Hard")))
            else:
                hard_data.append(0)

        X = np.arange(len(labels))
        width = 0.25

        fig, ax = plt.subplots()
        ax.bar(X - width/2, easy_data, width, label= 'Easy', color= 'g')
        ax.bar(X + width/2, medium_data, width, label= 'Medium', color= 'y')
        ax.bar(X + 3*width/2, hard_data, width, label= 'Hard', color= 'r')

        ax.set_ylabel('Scores')
        ax.set_title(f'Scores by {category}')
        plt.ylim(0, 30)
        ax.set_xticks(X + width / 2)
        ax.set_xticklabels(labels)
        plt.grid(color='grey', linestyle='-', linewidth=0.25)
        ax.legend()

        plt.show()






if __name__ == "__main__":

    filepath = r"C:\Users\vsbas\PycharmProjects\ECE homework 241 11\Stupid Projects\gun_skill_data.json"
    training_session = Testing_Ground()
    training_session.download_data(filepath)
    training_session.visualize_all_scores()
    # training_session.visualize_category("AR")
    training_session.practice_session_start()
    training_session.visualize_all_scores()
