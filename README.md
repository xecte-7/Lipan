# LIPAN

<a href="https://github.com/xecte-7/Lipan/releases"><img align="center" src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_help.png" alt="Lipan"></a>

## ABOUT
**[About Lipan]**<br>
*Lipan is a nested url crawler to help you gather every url related from the target*

**[About Author]**<br>
*Coded by Muhammad Rizky* a.k.a *XECTE-7*<br>
*I'm computer engineering college student at University of Borneo Tarakan that recently diagnosed with curiosity for cyber security and programming.*

**[Contact]**<br>
Instagram : *@muhammad.rizky98 / @portal_it.id / @xecte_7*<br>
Github : *github.com/xecte-7*<br>
HackerOne : *hackerone.com/xecte-7*<br>
YouTube : *Portal-IT ID*<br>
*#XECTE-7 #Portal_IT_ID #DariTeknikUntukDunia #HMTK_FT_UBT*

## INSTALLATION
Clone github repository to your desired location :<br>
> git clone https://github.com/xecte-7/Lipan<br>
Installing required modules :<br>
> cd Lipan/<br>
> python -m pip install -r requirements.txt<br>
Run Lipan :<br>
> python lipan.py --help<br>

## USAGE
**Help menu :**<br>
> python lipan.py --help<br>
*Expl: show help menu*<br>
**Basic crawling :**<br>
> python lipan.py -u "https://hackerone.com"<br>
*Expl: only set crawling starting point, the rest options will be set by default*<br>
**Full customized crawling :**<br>
> python crawling.py -u "https://hackerone.com" -d "api.hackerone.com" -i 3 -t 25 -o res_hackerone.txt<br>
*Expl: only focused on api.hackerone.com domain, crawling iteration is 3 and use 25 threading*<br>

## RELEASES
Check Lipan releases here :<br>
https://github.com/xecte-7/Lipan/releases/
<br>

## CHANGELOG
*> version 1.2*
- project name changed to "Lipan"
- renew source code
- can operate with more than 1 iteration
- adding thread option for faster work

*> version 1.1*
- renew source code
- adding user-friendly mode*

*> version 1.0*
- officially released to Github
- originally named "URL-Xtract"
- can operate with 1 iteration
