import requests

class PBSKidsAPI:
    BASE_URL = "https://producerplayer.services.pbskids.org/show-list?shows=almas-way%2Carthur%2Ccet-parents%2Ccetthinktv-education%2Ccity-island%2Cclifford-big-red-dog%2Ccliffords-puppy-days%2Ccrafts-kids%2Ccurious-george%2Ccyberchase%2Cdaniel-tigers-neighborhood%2Cdesign-squad-nation%2Cdinosaur-train%2Cdonkey-hodie%2Cdots-spot%2Celinor-wonders-why%2Cfetch-with-ruff-ruffman%2Cfamily-math%2Cfamily-math-en-espanol%2Cfizzys-lunch-lab%2Chero-elementary%2Cjamming-on-the-job%2Cjelly-ben-pogo%2Ckeyshawn-solves-it%2Clets-go-luna%2Clets-talk%2Cliteracy-tips-all-ages%2Clyla-loop%2Cmartha-speaks%2Cmaya-miguel%2Cmecha-builders%2Cmeet-helpers%2Cmega-wow%2Cmilo%2Cmister-rogers%2Cmolly-of-denali%2Cnature-cat%2Codd-squad%2Codd-tube%2Coh-noah%2Cpbs-kids%2Cpbs-kids-rocks%2Cpbs-kids-talk-about%2Cpbs-kids-activity-challenge%2Cpbs-kids-get-moving%2Cwestern-reserve-public-media-educational-productions%2Cparent-hacks%2Cparentalogic%2Cparenting-minutes%2Cpeg%2Cpinkalicious-and-peterrific%2Cplum-landing%2Cready-jet-go%2Crocket-saves-the-day%2Crosies-rules%2Csuper-why%2Cscigirls%2Cscribbles-and-ink%2Csearch-it-up%2Csesame-street%2Csid-science-kid%2Csplash-and-bubbles%2Csuper-whys-comic-book-adventures%2Ccat-in-the-hat%2Cnot-too-late-show-elmo%2Cruff-ruffman-show%2Cthrough-woods%2Ctiny-time-travel%2Cwosu-specials%2Cwhat-can-you-become%2Cwhats-good%2Cwild-kratts%2Cword-world%2Cword-of-the-week%2Cwordgirl%2Cwork-it-out-wombats%2Cxavier-riddle-and-secret-museum%2Cyou-me-community%2Ciq-smartparent&available=public"

    def __init__(self):
        pass

    def get_shows(self):
        response = requests.get(self.BASE_URL)
        response.raise_for_status()
        return response.json()["items"]

    def get_episodes_by_show(self, show_name):
        shows = self.get_shows()
        filtered_episodes = [
            show for show in shows if show.get("title").lower() == show_name.lower()
        ]
        return filtered_episodes
