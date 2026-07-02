# -*- coding: utf-8 -*-
import os
OUT = os.path.dirname(os.path.abspath(__file__))

MYCAUSE = "https://www.mycause.com.au/charity/47696/AustralianSportsBrainBank"
REDCAP = "https://redcap.slhd.nsw.gov.au/surveys/?s=HJFCHCHHL8JELFMH"
NEWSLETTER = "https://greenarrow.health.nsw.gov.au/ga/front/forms/114/subscriptions/new/"

NAV = [
    ("about.html", "About us"),
    ("resources.html", "Resources"),
    ("support.html", "Support us"),
    ("contact.html", "Contact"),
    ("https://greenarrow.health.nsw.gov.au/ga/front/forms/114/subscriptions/new/", "Newsletter"),
]

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
"%3Ccircle cx='8' cy='8' r='3' fill='%232b8a87'/%3E%3Ccircle cx='16' cy='8' r='3' fill='%23359a96'/%3E"
"%3Ccircle cx='24' cy='8' r='3' fill='%232b8a87'/%3E%3Ccircle cx='8' cy='16' r='3' fill='%23359a96'/%3E"
"%3Ccircle cx='16' cy='16' r='3' fill='%232b8a87'/%3E%3Ccircle cx='24' cy='16' r='3' fill='%23359a96'/%3E"
"%3Ccircle cx='8' cy='24' r='3' fill='%232b8a87'/%3E%3Ccircle cx='16' cy='24' r='3' fill='%23359a96'/%3E"
"%3Ccircle cx='24' cy='24' r='3' fill='%232b8a87'/%3E%3C/svg%3E")


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Australian Sports Brain Bank</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#2b8a87">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} — Australian Sports Brain Bank">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="Australian Sports Brain Bank">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<a href="#main" class="skip" style="position:absolute;left:-9999px">Skip to content</a>
"""


def header(active):
    return """<header>
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="Sports Brain Bank — home">
      <img class="logo-img" src="assets/img/logo.png" alt="Sports Brain Bank">
    </a>
    <nav id="nav" aria-label="Primary">
      <ul>
        <li><a href="about.html">About us</a></li>
        <li><a href="why-pledge.html">Why pledge</a></li>
        <li><a href="make-a-pledge.html">Make a pledge / donate</a></li>
        <li class="has-sub">
          <a href="resources.html" aria-haspopup="true">Resources <span class="caret" aria-hidden="true">&#9662;</span></a>
          <ul class="submenu">
            <li><a href="cte-diagnosis.html">CTE diagnosis</a></li>
            <li><a href="cte-research.html">CTE research</a></li>
            <li><a href="publications.html">Our publications</a></li>
            <li><a href="resources.html">Downloadable resources</a></li>
          </ul>
        </li>
        <li><a href="in-the-media.html">In the media</a></li>
        <li><a href="support.html">Support us</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
"""


def page_hero(title, sub, crumb=True):
    c = '      <div class="crumb"><a href="index.html">Home</a> / ' + title + '</div>\n' if crumb else ''
    s = f'      <p>{sub}</p>\n' if sub else ''
    return f"""<section class="page-hero">
    <div class="wrap">
{c}      <h1>{title}</h1>
{s}    </div>
</section>
<main id="main">
"""


FOOTER = """</main>
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h3>Australian Sports<br>Brain Bank</h3>
        <p class="tagline">Researching towards a world without CTE</p>
      </div>
      <div>
        <h4>Media Enquiries</h4>
        <p>0409 243 544<br><a href="mailto:slhd-media@health.nsw.gov.au">slhd-media@health.nsw.gov.au</a></p>
        <h4>Mailing Address</h4>
        <p>Australian Sports Brain Bank<br>94 Mallett Street<br>Camperdown NSW 2050</p>
        <h4>Email</h4>
        <p><a href="mailto:SLHD-brainbank@health.nsw.gov.au">SLHD-brainbank@health.nsw.gov.au</a></p>
        <h4>Telephone</h4>
        <p>(02) 9351 0943</p>
      </div>
      <div>
        <p class="foot-note">In the event of a donor death, please contact your appointed funeral director in the first instance and follow their normal processes.</p>
        <p class="foot-note" style="margin-top:14px">If death occurs during the night, please notify us the following morning so that we can progress the brain donation. We will liaise directly with your appointed funeral directors to ensure that the donation occurs in a timely and efficient manner.</p>
        <p class="foot-note" style="margin-top:14px">We are available if required <span class="hl">24 hours 7 days a week</span> by calling our paging service on <span class="hl">1800 551 898</span></p>
      </div>
    </div>
    <div class="foot-bottom">© 2026 Australian Sports Brain Bank. All rights reserved.</div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""


def build(filename, active, title, desc, hero_sub, body):
    html = head(title, desc) + header(active) + page_hero(title, hero_sub) + body + FOOTER
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html), "chars")


HEADSHOTS = {
    'MB':'michael-buckland.jpg','MC':'monica-clarke.jpg','CS':'catherine-suter.jpg',
    'AP':'alan-pearce.jpg','JC':'jennifer-cropley.jpg','LI':'linda-iles.jpg',
    'AG':'amanda-green.jpg','RT':'renee-tuck.jpg','PF':'peter-fitzsimons.jpg','AF':'anita-frawley.jpg',
}
def person(initials, name, role, text):
    img = HEADSHOTS.get(initials)
    if img:
        pic = f'<div class="pic"><img src="assets/img/{img}" alt="{name}"></div>'
    else:
        pic = f'<div class="pic" aria-hidden="true">{initials}</div>'
    return f"""    <div class="person">
      {pic}
      <div>
        <h3>{name}</h3>
        <div class="role">{role}</div>
        <p>{text}</p>
      </div>
    </div>
"""

# ---------------------------------------------------------------- ABOUT
team = [
    ("MB","Michael Buckland","Founding &amp; Executive Director",
     "A senior neuropathologist and Head of the Department of Neuropathology at Royal Prince Alfred Hospital, Head of the Molecular Neuropathology Program at the Brain &amp; Mind Centre, University of Sydney, and Co-Director of the Multiple Sclerosis Research Australia Brain Bank."),
    ("LI","Linda Iles","Forensic Pathologist",
     "Forensic pathologist at the Victorian Institute of Forensic Medicine (VIFM), where she has been Head of forensic pathology services for the past ten years. She has an interest in forensic neuropathology and post-mortem radiological imaging in forensic pathology practice."),
    ("CS","Catherine Suter","Chief Scientist",
     "Responsible for the direction and scientific integrity of ASBB tissue research. A world-recognised expert on environmental influence on disease risk, particularly epigenetics, she brings this expertise to the study of CTE to understand the disease and develop ways to diagnose it during life."),
    ("JC","Jennifer Cropley","Data Scientist",
     "A senior research scientist expert in the analysis of large datasets. She brings her experience to the ASBB to spearhead population-based studies on the long-term outcomes of concussion and repeated head injuries in contact sports."),
    ("AP","Alan Pearce","Research Manager — Victoria",
     "A neurophysiologist who has spent 20 years researching sports-related concussion. Using electrophysiological techniques, particularly transcranial magnetic stimulation, his research centres on brain physiology to quantify cognitive and motor impairments in the acute phase post-concussion and the chronic manifestations of repeated concussions."),
    ("MC","Monica Clarke (RN)","Brain Donation Specialist Nurse",
     "A clinical nurse consultant with a background in organ transplant coordination. With over 15 years of clinical nursing experience, she is committed to improving future outcomes through ongoing research, while providing compassionate advocacy, support and education for individuals and families affected by CTE."),
]
ambassadors = [
    ("AG","Amanda Green","Ambassador",
     "Wife of the late NRL player and coach Paul Green, Amanda is passionate about raising awareness of CTE and its symptoms so no one else suffers in silence. With two young sports-loving children, she understands firsthand the importance of the ASBB's research for the next generation of athletes."),
    ("RT","Renee Tuck","Families Ambassador",
     "As sister of the late AFL player Shane Tuck, Renee has lived experience of how CTE can impact families. She generously donates her time to the ASBB to help educate and raise awareness, and feels passionately about supporting other families going through loss due to this disease."),
    ("AF","Anita Frawley","Ambassador",
     "Wife of the late AFL player and coach Danny Frawley, Anita was determined to find answers to her husband's mental health struggles. She is passionate about prioritising care for retired athletes, and protecting and supporting current athletes during their careers."),
    ("PF","Peter FitzSimons","Ambassador",
     "Former Wallaby Peter FitzSimons is a vocal advocate for player safety and stricter concussion management in Australian contact sports. His stance has generated widespread debate, particularly regarding the long-term impacts of repeated head impacts and the risk of CTE. He advocates for drastic structural changes to make contact sports safer, including the total banning of the kick-off in rugby league to avoid initial, high-impact collisions."),
]
about_body = f"""<section>
  <div class="wrap prose">
    <p>The ASBB was established in 2018 by the <a href="https://www.slhd.nsw.gov.au/RPA/Neuropathology/default.html" target="_blank" rel="noopener">Neuropathology Department at RPA Hospital Sydney</a> in partnership with the <a href="https://sydney.edu.au/brain-mind/" target="_blank" rel="noopener">Brain and Mind Centre at the University of Sydney</a>, and the <a href="https://concussionfoundation.org/" target="_blank" rel="noopener">Concussion Legacy Foundation in the USA</a>.</p>
    <h2>Our Mission</h2>
    <p>Our mission is to use expert diagnostic neuropathology, coupled with research, to understand chronic traumatic encephalopathy (CTE) and other brain pathology that is associated with repetitive head injury in sport and elsewhere. We empower families and loved ones by providing accurate diagnoses, and we use donor tissue for biomedical research into CTE and other brain disorders.</p>
    <h2>Our Vision</h2>
    <p>Our vision is for Australia to be a nation that recognises and acts on CTE and other brain disorders associated with repetitive head injury. We will provide help and advocacy for those individuals and families affected. We are working to achieve our vision through:</p>
    <ul>
      <li><strong>Educating</strong> the public and medical practitioners about CTE</li>
      <li><strong>Connecting</strong> affected families to create a support network</li>
      <li><strong>Facilitating</strong> world-class research on CTE through our brain donor program</li>
    </ul>
  </div>
</section>
<section class="section-mint">
  <div class="wrap">
    <h2 class="center">Our Team</h2>
    <p class="lead center">The clinicians and scientists behind the Australian Sports Brain Bank.</p>
    <div class="people">
{''.join(person(*p) for p in team)}    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <h2 class="center">Our Ambassadors</h2>
    <p class="lead center">Advocates with lived experience, helping raise awareness of CTE.</p>
    <div class="people">
{''.join(person(*p) for p in ambassadors)}    </div>
    <div class="center" style="margin-top:36px"><a class="btn btn-solid" href="make-a-pledge.html">Make a pledge</a></div>
  </div>
</section>
"""
build("about.html","about.html","About Us",
      "Our mission is to understand chronic traumatic encephalopathy in the Australian population.",
      "Our mission is to understand chronic traumatic encephalopathy in the Australian population.",
      about_body)

# ---------------------------------------------------------------- WHY PLEDGE
why_body = """<section>
  <div class="wrap prose">
    <p>Our knowledge on the long-term effects of concussion and other traumatic injuries to the brain is in its infancy. There are several neurological conditions that may be related to repeated concussions and sub-concussive injuries, and while modern technologies such as brain scanning can detect some brain diseases, definitive diagnosis requires analysis of actual brain tissue.</p>
    <p>Since the launch of the Australian Sports Brain Bank in March 2018, we have identified chronic traumatic encephalopathy (CTE) in dozens of individuals, but at this stage we do not know how common it is, or how to diagnose it during life.</p>
    <p>Only through examining the brains of many Australian sportspeople — with and without a history of concussion or other traumatic brain injuries, from amateur to professional levels — will we know the extent of the issue in the Australian sporting population.</p>
    <p>By donating your brain to the ASBB after your death, your family (or nominated person) will receive a comprehensive neuropathology report detailing any brain disease present. But most importantly, your donation will help us understand the cellular and molecular changes in the brain that may occur with repeated concussions or sub-concussive injuries.</p>
    <p>By gathering this information, our sporting communities will be able to make well-informed policy and effective guidelines for the prevention, identification and, potentially, treatment of concussion and CTE in Australian communities.</p>
    <div class="callout"><p>Pledging your brain is a profound act of generosity. Every pledge brings us closer to understanding, diagnosing and one day preventing CTE.</p></div>
    <div class="btn-row">
      <a class="btn btn-solid" href="make-a-pledge.html">Make a pledge</a>
      <a class="btn" href="cte-research.html">Read about our research</a>
    </div>
  </div>
</section>
"""
build("why-pledge.html","why-pledge.html","Why pledge your brain?",
      "Why donating your brain to research matters for the future of brain health in Australian sport.",
      "An act of generosity that helps shape the future of brain health in Australian sport.",
      why_body)

# ---------------------------------------------------------------- MAKE A PLEDGE
pledge_body = f"""<section>
  <div class="wrap prose">
    <h2>Help us understand CTE</h2>
    <p>If you think you might like to donate your brain to the ASBB after your death, please click the link below to make your pledge and have an information pack sent to you. The information pack will contain the forms you will need to fill out and return to us to make sure your pledge is fulfilled.</p>
    <div class="callout"><p>All enquiries will be kept <strong>strictly confidential</strong>.</p></div>
    <div class="btn-row">
      <a class="btn btn-solid" href="{REDCAP}" target="_blank" rel="noopener">Pledge your brain to research</a>
      <a class="btn" href="why-pledge.html">Why pledge?</a>
    </div>
    <h3 style="margin-top:38px">Questions?</h3>
    <p>If you have any questions about pledging, our team is here to help. Email us at <a href="mailto:SLHD-brainbank@health.nsw.gov.au">SLHD-brainbank@health.nsw.gov.au</a> or call (02) 9351 0943.</p>
  </div>
</section>
"""
build("make-a-pledge.html","make-a-pledge.html","Make a pledge",
      "Pledge your brain to the Australian Sports Brain Bank and help us understand CTE.",
      "Help us understand CTE by pledging your brain to research.",
      pledge_body)

# ---------------------------------------------------------------- CTE DIAGNOSIS
diag_body = """<section>
  <div class="wrap prose">
    <p class="date">Statement — 29 March 2023</p>
    <p>Chronic traumatic encephalopathy (CTE) is the name given to a pathology that is found in the brains of some people exposed to repetitive head injuries. The ASBB is dedicated to the understanding of CTE.</p>
    <p>Many people have already donated or pledged their brains to us at the ASBB, and this generous gift is enabling research to better understand this disease. Our mission at the ASBB is to use and promote research to help diagnose, prevent, monitor and treat CTE. At the heart of our goals is the development of clinical tests that can diagnose CTE in people while they are living.</p>
    <p>The ASBB is aware of recent public statements suggesting that CTE can be diagnosed in people who are still living. This has caused confusion and sometimes distress amongst our brain pledgers and the families of our brain donors. At present the definitive diagnosis of CTE remains one that can only be made after death, and together with our pledgers and donor families we are working to change this.</p>
    <div class="callout"><p><strong>There are currently NO tests that can diagnose CTE during life.</strong> The symptoms we believe may be caused by CTE can overlap with many other conditions, and many of them are treatable. In some cases, CTE has been found in people who experienced no symptoms at all.</p></div>
    <p>Criteria for a clinical syndrome, Traumatic Encephalopathy Syndrome (TES), are being developed to help researchers understand the potential symptoms caused by CTE during life. The creators of the TES criteria have encouraged the medical community to only use them in research settings, as they are not yet accurate enough to deploy in the clinic.</p>
    <p>PET scanning has been proposed by some as a way to diagnose CTE. Unfortunately, this is not true. PET is a powerful tool that can reveal abnormalities in the brain, but it is not yet able to test for CTE. We are actively working in this area to try and change this.</p>
    <h3>Where to find support</h3>
    <p>If you or a loved one would like additional education on CTE, or a referral to a provider trained to support individuals exposed to concussions or repetitive head impacts, please reach out to our collaborators at the Concussion Legacy Foundation Australia via their <a href="https://concussionandcte.org/en-au/helpline/" target="_blank" rel="noopener">HelpLine</a> or via <a href="mailto:help@concussionandcte.org">email</a>.</p>
    <p>If you feel like you may be in crisis and would like to talk to someone, please call <a href="https://www.lifeline.org.au/" target="_blank" rel="noopener">Lifeline</a> on <strong>13 11 14</strong>.</p>
    <h3>Further reading</h3>
    <ul>
      <li><a href="https://www.rcpa.edu.au/Library/Publications/PathWay/Docs/New-RCPA-position-statement-on-chronic-traumatic-e" target="_blank" rel="noopener">2023 RCPA position statement on chronic traumatic encephalopathy</a></li>
      <li><a href="publications.html">ASBB peer-reviewed publications on CTE</a></li>
    </ul>
  </div>
</section>
"""
build("cte-diagnosis.html","cte-diagnosis.html","Diagnosis of CTE during life",
      "The ASBB statement on the diagnosis of CTE during life.",
      "The ASBB statement on the diagnosis of CTE during life.",
      diag_body)

# ---------------------------------------------------------------- CTE RESEARCH
research_body = """<section>
  <div class="wrap prose">
    <h2>Diagnosis and Research</h2>
    <p>Despite technical advances in clinical medicine, the only way to definitively diagnose many types of brain disease is by examination of brain tissue after death. This is particularly the case for chronic traumatic encephalopathy (CTE): at present there is no test a doctor can perform that will allow them to diagnose CTE while you are living. We at the ASBB are working to change that.</p>
    <p>Researchers overseas have attempted to define some clinical criteria for a condition called traumatic encephalopathy syndrome (TES) that is associated with repetitive head injuries, and this may be related to CTE in some individuals. But these TES criteria are only intended for use in research studies, and a diagnosis of TES does not mean a diagnosis of CTE.</p>
    <h2>What is CTE?</h2>
    <p>CTE is a brain condition that is caused by repeated exposure to mild traumatic brain injuries. These may or may not be associated with concussion. CTE was first found in boxers many decades ago, and has since been described in players of American football and a host of other contact sports where head injuries occur regularly.</p>
    <p>The Australian Sports Brain Bank found the first cases of CTE in ex-players of Australian Rules football, rugby league and rugby union, so we know that Australia is not immune to this disease. It is important to know that not everyone who experiences repeated mild traumatic brain injuries will develop CTE. We do not currently understand why this is the case.</p>
    <p>CTE can occur at any age, and in most cases the first symptoms occur years or decades after brain injury. Signs of CTE include problems with thinking and memory, personality changes, and behavioural changes including aggression and depression. Up-to-date information on the science of CTE, concussion and persistent post-concussion syndrome can be found on the <a href="https://concussionfoundation.org/" target="_blank" rel="noopener">Concussion Legacy Foundation</a> website. The CLF are our international partners. Please also see our <a href="resources.html">Resources</a> page for other materials on CTE.</p>
    <h2>What is the ASBB trying to achieve?</h2>
    <p>We do not currently know how often CTE or any other brain disease occurs in Australian contact sportspeople across different sports. A primary goal of the ASBB is to confirm the existence — and evaluate the prevalence — of CTE in Australian contact sports, and make this information available to the public and to policy makers.</p>
    <p>The ASBB is committed to research into the long-term effects of concussion on the brain, in particular with regard to CTE, with a view to developing new means of diagnosing brain disease during life. This research involves understanding the full impact of sports-related concussion on the human nervous system, and would not be possible without the tissue so generously given by our donors and their families.</p>
    <p>We are using donated tissue to try to understand why some individuals get CTE and others don't. There may be genetic factors, as well as environmental risk factors, involved. Studying donor tissue helps us understand the biological processes involved in the development of CTE, which will lead to tests that can diagnose CTE in life and help develop effective treatments.</p>
    <p>ASBB neuropathologists are expert in tissue-based diagnosis of all brain pathology, including CTE. A comprehensive neuropathological evaluation of brains donated to the ASBB is provided to a doctor nominated by the family so that the results can be discussed. Together, the diagnoses of all brains donated to the ASBB help us inform the community on the nature and extent of brain pathology associated with contact sports in Australia.</p>
    <div class="btn-row">
      <a class="btn btn-solid" href="publications.html">View our publications</a>
      <a class="btn" href="make-a-pledge.html">Make a pledge</a>
    </div>
  </div>
</section>
"""
build("cte-research.html","cte-research.html","CTE Research",
      "How the Australian Sports Brain Bank researches the diagnosis, causes and prevention of CTE.",
      "Understanding the diagnosis, causes and prevention of chronic traumatic encephalopathy.",
      research_body)

# ---------------------------------------------------------------- PUBLICATIONS
PUBS = {
 "2019":[("Chronic traumatic encephalopathy in two former Australian National Rugby League players","Acta Neuropathologica Communications","https://actaneurocomms.biomedcentral.com/articles/10.1186/s40478-019-0751-1")],
 "2020":[("Chronic traumatic encephalopathy in a former Australian rules football player diagnosed with Alzheimer's disease","Acta Neuropathologica Communications","https://actaneurocomms.biomedcentral.com/articles/10.1186/s40478-020-0895-z")],
 "2021":[("Effects of Stricter Management Guidelines on Return-to-Competition Timeframes Following Concussion in Professional Australian Rules Football: An Exploratory Analysis","Sports Medicine","https://link.springer.com/article/10.1007/s40279-021-01484-z"),
         ("Toward complete, candid, and unbiased International consensus statements on concussion in sport","J Law Med Ethics","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8941977/"),
         ("Chronic Neurophysiological Effects of Repeated Head Trauma in Retired Australian Male Sports Athletes","Frontiers in Neurology","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7985524/")],
 "2022":[("Chronic traumatic encephalopathy in Australia: the first three years of the Australian Sports Brain Bank","Medical Journal of Australia","https://onlinelibrary.wiley.com/doi/10.5694/mja2.51420"),
         ("Chronic Traumatic Encephalopathy as a Preventable Environmental Disease","Frontiers in Neurology","https://www.frontiersin.org/articles/10.3389/fneur.2022.880905/full"),
         ("Applying the Bradford Hill Criteria for Causation to Repetitive Head Impacts and Chronic Traumatic Encephalopathy","Frontiers in Neurology","https://www.frontiersin.org/articles/10.3389/fneur.2022.938163/full"),
         ("Tau Pathology in Chronic Traumatic Encephalopathy is Primarily Neuronal","J Neuropathol Exp Neurol","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9487650/"),
         ("Chronic Traumatic Encephalopathy in a Routine Neuropathology Service in Australia","J Neuropathol Exp Neurol","https://pubmed.ncbi.nlm.nih.gov/35947764/")],
 "2023":[("Assessment of Somatosensory and Motor Processing Time in Retired Athletes with a History of Repeated Head Trauma","J Funct Morphol Kinesiol","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9782447/"),
         ("Chronic Traumatic Encephalopathy (CTE) — Features and Considerations","Forensic Sci Med Pathol","https://pubmed.ncbi.nlm.nih.gov/37058211/"),
         ("Chronic Traumatic Encephalopathy in a female ex-professional Australian rules footballer","Acta Neuropathologica","https://link.springer.com/article/10.1007/s00401-023-02610-z"),
         ("Risk of chronic traumatic encephalopathy in rugby union is associated with length of playing career","Acta Neuropathologica","https://link.springer.com/article/10.1007/s00401-023-02644-3")],
 "2024":[("Chronic traumatic encephalopathy in the context of intimate partner violence","Acta Neuropathologica","https://pmc.ncbi.nlm.nih.gov/articles/PMC11230984/")],
 "2025":[("Spatially resolved transcriptomics reveals a unique disease signature and potential biomarkers for chronic traumatic encephalopathy","J Neuropathol Exp Neurol","https://academic.oup.com/jnen/advance-article/doi/10.1093/jnen/nlaf078/8206318?login=false"),
         ("The neuropathology of chronic traumatic encephalopathy","Pathology","https://www.pathologyjournal.rcpa.edu.au/article/S0031-3025(24)00715-3/fulltext"),
         ("Perivascular glial reactivity is a feature of phosphorylated tau lesions in chronic traumatic encephalopathy","Acta Neuropathologica","https://pmc.ncbi.nlm.nih.gov/articles/PMC11807024/")],
}
pub_html = '<section>\n  <div class="wrap prose">\n    <p>Scientific papers resulting from the work of the Australian Sports Brain Bank and our collaborators. Click any title to read the publication.</p>\n'
for yr in sorted(PUBS.keys(), reverse=True):
    pub_html += f'    <div class="pub-year">{yr}</div>\n    <ul class="pub-list">\n'
    for title, journal, url in PUBS[yr]:
        pub_html += f'      <li class="pub"><a href="{url}" target="_blank" rel="noopener">{title}</a><span class="journal">{journal}</span></li>\n'
    pub_html += '    </ul>\n'
pub_html += '  </div>\n</section>\n'
build("publications.html","publications.html","Our Publications",
      "Peer-reviewed scientific publications from the Australian Sports Brain Bank, 2019 to 2025.",
      "Peer-reviewed research from the ASBB and our collaborators.",
      pub_html)

# ---------------------------------------------------------------- PARTNERS
JIM = "https://image.jimcdn.com/app/cms/image/transf/none/path/s3eb0dce32a7e31d8/image/"
partner_logos = [
 JIM + "i2be21d4df06357fd/version/1588560191/image.png",
 JIM + "i80f2b0a9c5a252b0/version/1588560191/image.jpg",
 JIM + "ifc56bc3b93711f6d/version/1588560191/image.png",
 JIM + "i6806a27f494d0c13/version/1588560191/image.jpg",
 JIM + "i458dbdeda8795d49/version/1588560191/image.png",
 JIM + "ib70304e8b32046c6/version/1588560191/image.png",
 JIM + "i7b4c8e69cf4fdab5/version/1637282070/image.png",
]
cards = "".join(f'      <div class="partner-card"><img src="{u}" alt="ASBB partner logo" loading="lazy"></div>\n' for u in partner_logos)
partners_body = f"""<section>
  <div class="wrap">
    <p class="lead center">The Australian Sports Brain Bank is a proud partnership. We gratefully acknowledge the institutions, organisations and supporters who make our work possible.</p>
    <div class="partner-grid">
{cards}    </div>
    <div class="center" style="margin-top:40px"><a class="btn btn-solid" href="support.html">Support our work</a></div>
  </div>
</section>
"""
build("partners.html","partners.html","Our Partners &amp; Supporters",
      "The institutions and organisations who partner with and support the Australian Sports Brain Bank.",
      "The institutions and organisations who make our work possible.",
      partners_body)

# ---------------------------------------------------------------- SUPPORT
support_body = f"""<section>
  <div class="wrap prose">
    <h2>Help support our research</h2>
    <p>You can help support our work by making a donation. All donations, however small, are welcome — and they are tax deductible. When you donate you will be directed to the secure donations portal of MyCause.</p>
    <div class="btn-row">
      <a class="btn btn-solid" href="{MYCAUSE}" target="_blank" rel="noopener">Donate to CTE research</a>
    </div>
    <p style="margin-top:24px">If you wish to make a donation <em>in memoriam</em>, please leave a comment in the donation box, or alternatively contact us directly at <a href="mailto:SLHD-brainbank@health.nsw.gov.au">SLHD-brainbank@health.nsw.gov.au</a>.</p>
  </div>
</section>
<section class="section-mint">
  <div class="wrap prose">
    <h2>Steigen × ASBB — SOCKS4SAM</h2>
    <p>The ASBB and our friends at the <a href="https://geelongsportsmedicinecentre.com.au/" target="_blank" rel="noopener">Geelong Sports Medicine Centre</a> have partnered with Steigen to honour the life of Sam McMahon, who passed away in 2021 with CTE. Each step taken in these limited-edition socks supports vital research into CTE. All profits go directly to ASBB research.</p>
    <div class="btn-row">
      <a class="btn btn-solid" href="https://asbbsocksforsam.com/" target="_blank" rel="noopener">Buy your socks</a>
      <a class="btn" href="partners.html">Our partners</a>
    </div>
  </div>
</section>
"""
build("support.html","support.html","Support Us",
      "Donate to help us understand chronic traumatic encephalopathy (CTE). All donations are tax deductible.",
      "Donate to help us understand chronic traumatic encephalopathy (CTE).",
      support_body)

# ---------------------------------------------------------------- RESOURCES
resources_body = f"""<section>
  <div class="wrap prose">
    <h2>Understanding CTE</h2>
    <p>Information and research on chronic traumatic encephalopathy (CTE) from the Australian Sports Brain Bank.</p>
    <ul>
      <li><a href="cte-diagnosis.html">Our statement on the diagnosis of CTE during life</a></li>
      <li><a href="cte-research.html">What is CTE, and our research</a></li>
      <li><a href="publications.html">Our peer-reviewed publications</a></li>
    </ul>
    <h2>Pledge &amp; support</h2>
    <ul>
      <li><a href="why-pledge.html">Why pledge your brain?</a></li>
      <li><a href="{REDCAP}" target="_blank" rel="noopener">Make a pledge</a> — via the NSW Health ethics-approved form</li>
      <li><a href="{MYCAUSE}" target="_blank" rel="noopener">Donate to research</a> — secure MyCause portal (Royal Prince Alfred Hospital)</li>
      <li><a href="{NEWSLETTER}" target="_blank" rel="noopener">Subscribe to our e-newsletter</a></li>
    </ul>
  </div>
</section>
<section class="section-mint">
  <div class="wrap prose">
    <h2>Downloadable resources</h2>
    <p>Materials tailored to different audiences. Downloadable PDFs will be available here:</p>
    <ul>
      <li>Resources for <strong>students</strong> — clear, non-academic explanations for school assignments and learning.</li>
      <li>Resources for <strong>athletes and families</strong> — for those who are curious or concerned about CTE.</li>
      <li>Resources for <strong>medical and health professionals</strong> — more detailed clinical information.</li>
      <li>Resources for <strong>researchers</strong> — technical materials and references.</li>
      <li>The US Centre for Disease Control (CDC) CTE factsheet.</li>
    </ul>
    <h3>Other useful information</h3>
    <p>Up-to-date information on the science of CTE, concussion and persistent post-concussion syndrome can be found via our international partners at the <a href="https://concussionfoundation.org/" target="_blank" rel="noopener">Concussion Legacy Foundation</a>, and locally via the <a href="https://concussionandcte.org/en-au/" target="_blank" rel="noopener">Concussion &amp; CTE Foundation Australia</a>.</p>
    <p>If you feel like you may be in crisis and would like to talk to someone, please call <a href="https://www.lifeline.org.au/" target="_blank" rel="noopener">Lifeline</a> on <strong>13 11 14</strong>.</p>
  </div>
</section>
"""
build("resources.html","resources.html","Resources",
      "CTE information, pledge and donation options, and downloadable resources from the Australian Sports Brain Bank.",
      "CTE information, ways to pledge and support, and downloadable materials.",
      resources_body)

# ---------------------------------------------------------------- IN THE MEDIA
media = [
 ("aHShkmUdx4E","Four Corners","Collision","2026"),
 ("lf0OQgH0vUs","A Current Affair","RunIt","2025"),
 ("6-nhJNnoMng","ABC 7.30","First female athlete diagnosed with CTE","2023"),
 ("cSNSx8q6ZSA","10 News","Paul Green's CTE diagnosis","2023"),
 ("0CLc4r6LSpM","A Current Affair","His brain had been taken over","2023"),
 ("_L-2XfKjimE","60 Minutes","Mind Matters","2021"),
 ("H6l1jZIM8gg","Sky News Australia","AFL players at higher risk of developing CTE","2020"),
]
media_cards = ""
for vid,outlet,title,year in media:
    thumb = f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"
    url = f"https://www.youtube.com/watch?v={vid}"
    media_cards += f"""      <a class="res-card" href="{url}" target="_blank" rel="noopener">
        <div class="thumb" aria-hidden="true" style="background-image:url('{thumb}')"></div>
        <div class="body"><h3>{title}</h3><p>{outlet} &middot; {year}</p><span class="watch">Watch on YouTube &rarr;</span></div>
      </a>
"""
media_body = f"""<section>
  <div class="wrap">
    <div class="prose"><p>The Australian Sports Brain Bank and its work have featured across major Australian media. A selection of appearances covering CTE research, advocacy, and the families affected.</p></div>
    <div class="res-cards">
{media_cards}    </div>
  </div>
</section>
"""
build("in-the-media.html","in-the-media.html","In the Media",
      "The Australian Sports Brain Bank in the media — CTE coverage and appearances across Australian television.",
      "The Australian Sports Brain Bank across major Australian media.",
      media_body)

# ---------------------------------------------------------------- CONTACT
contact_body = """<section>
  <div class="wrap">
    <div class="alert" role="note">
      <p><strong>In the event of a donor death</strong>, please contact your appointed funeral director in the first instance and follow their normal processes.</p>
      <p style="margin-top:12px">If death occurs during the night, please notify us the following morning so that we can progress the brain donation. We will liaise directly with your appointed funeral directors to ensure that the donation occurs in a timely and efficient manner.</p>
      <p style="margin-top:12px">We are available if required <span class="hl">24 hours, 7 days a week</span> by calling our paging service on <span class="hl">1800 551 898</span>.</p>
    </div>
    <div class="contact-grid">
      <div class="contact-card">
        <h3>Get in touch</h3>
        <h4>General &amp; brain bank enquiries</h4>
        <p><a href="mailto:SLHD-brainbank@health.nsw.gov.au">SLHD-brainbank@health.nsw.gov.au</a><br>(02) 9351 0943</p>
        <h4>Media enquiries</h4>
        <p>0409 243 544<br><a href="mailto:slhd-media@health.nsw.gov.au">slhd-media@health.nsw.gov.au</a></p>
        <h4>Paging service (24/7)</h4>
        <p>1800 551 898</p>
      </div>
      <div class="contact-card">
        <h3>Visit us</h3>
        <h4>Mailing address</h4>
        <p>Australian Sports Brain Bank<br>94 Mallett Street<br>Camperdown NSW 2050</p>
        <h4>Make a pledge</h4>
        <p>Ready to pledge your brain to research? <a href="make-a-pledge.html">Start your pledge here</a>.</p>
        <h4>Support our work</h4>
        <p>Donations are tax deductible. <a href="support.html">Donate to CTE research</a>.</p>
      </div>
    </div>
  </div>
</section>
"""
build("contact.html","contact.html","Contact",
      "Contact the Australian Sports Brain Bank, including 24/7 donor death notification details.",
      "How to reach the Australian Sports Brain Bank.",
      contact_body)

print("ALL PAGES BUILT")
