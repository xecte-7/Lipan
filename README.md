<a href="https://github.com/xecte-7/Lipan/releases"><img align="center" src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_banner.png" alt="Lipan"></a>

# LIPAN
*Lipan is a nested url crawler to help you gather every url related from the target*


### INSTALLATION
> Clone github repository to your desired location :<br>
> 
> > git clone https://github.com/xecte-7/Lipan
> > cd Lipan/<br>
> 
> Installing required modules (python pip) :<br>
> 
> > python -m pip install -r requirements.txt
> 
> Installing required modules (linux apt) :
> 
> > sudo apt install python3-requests python3-bs4
> 
> Run Lipan :<br>
> > python lipan.py --help

### USAGE
> **Help menu :**<br>
> *Show help menu*<br>
> 
> > python lipan.py --help
> 
> **Basic crawling :**<br>
> *Only set crawling starting point, the rest options will be set by default*<br>
> 
> > python lipan.py -u "https://hackerone.com"
> 
> **Customized crawling :**<br>
> *Domain scope focused on api.hackerone.com, crawling iteration is 3 and use 25 threading*<br>
> 
> > python crawling.py -u "https://hackerone.com" -d "api.hackerone.com" -i 3 -t 25 -o res_hackerone.txt

### PREVIEW
<details>
  <summary>Help Menu Preview</summary>
  <img src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_help.png" name="help-menu">
</details>
<details>
  <summary>Running Preview</summary>
  <img src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_demo1.png" name="preview-1">
  <img src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_demo2.png" name="preview-2">
  <img src="https://raw.githubusercontent.com/xecte-7/projects-assets/main/Lipan/version-1.2/lipan_demo3.png" name="preview-3">
</details>

### RELEASES
Check Lipan releases here :<br>
https://github.com/xecte-7/Lipan/releases/
<br>

### ABOUT AUTHOR
> **[About Me]**<br>
> *Coded by Muhammad Rizky* a.k.a *XECTE-7*<br>
> *I'm computer engineering college student at University of Borneo Tarakan that recently diagnosed with > curiosity for cyber security and programming.*
> 
> **[Contact]**<br>
> Instagram : *@muhammad.rizky98 / @portal_it.id / @xecte_7*<br>
> Github : *github.com/xecte-7*<br>
> HackerOne : *hackerone.com/xecte-7*<br>
> YouTube : *Portal-IT ID*<br>
> *#XECTE-7 #Portal_IT_ID #DariTeknikUntukDunia #HMTK_FT_UBT*

### CHANGELOG
> - version 1.2
> 	- changed project name to "Lipan"
> 	- renew source code
> 	- can operate with specified number of iteration
> 	- adding thread option (min-max: 1-50)
> 	- adding domain option for filtering domain scope
> 	- adding save output option
> 	- adding verbosity option
> 
> - version 1.1
> 	- renew source code
> 	- adding user-friendly mode*
> 
> - version 1.0
> 	- officially released to Github
> 	- originally named "URL-Xtract"
> 	- can operate with 1 iteration
