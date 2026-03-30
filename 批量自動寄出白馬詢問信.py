import os
import subprocess

hotels = [
  {"name": "Mountain Side Hakuba", "email": "info@mountainsidehakuba.com"},
  {"name": "Koharu Resort Hotel", "email": "info@koharuresort.com"},
  {"name": "Phoenix Chalets", "email": "bookings@hakubahotelgroup.com"},
  {"name": "Ryokan Shirouma-So", "email": "info@shiroumaso.com"},
  {"name": "Hakuba Panorama Hotel", "email": "info@hakuba-panorama.com"},
  {"name": "Hakuba Yamano Hotel", "email": "info@hakuba-yamanohotel.com"},
  {"name": "Black Bear Apartments", "email": "info@blackbearhakuba.com"},
  {"name": "The Ridge Hakuba", "email": "info@theridgehakuba.com"},
  {"name": "Roka Apartments", "email": "contact@rokahakuba.com"},
  {"name": "Slopeside Chalets", "email": "info@slopesidechalets.com"},
  {"name": "Wadano Gateway Suites", "email": "info@wadanogateway.com"},
  {"name": "Happo View Chalet", "email": "stay@happoviewchalet.com"},
  {"name": "Hakuba Powder Cottage", "email": "info@hakubapowdercottage.com"},
  {"name": "Hotel Sierra Resort Hakuba", "email": "info@sierra.ne.jp"},
  {"name": "Penke Panke Lodge", "email": "info@penkepanke.com"},
  {"name": "Ryokan Biyu no Yado", "email": "info@biyunoyado.com"},
  {"name": "Aria Hotel Hakuba", "email": "info@ariahotelhakuba.com"},
  {"name": "Shirouma Village", "email": "info@shiroumavillage.com"},
  {"name": "Villa Hakuba", "email": "info@villahakuba.com"},
  {"name": "Aura Chalets", "email": "bookings@hakubahotelgroup.com"},
  {"name": "Powder Suites", "email": "info@powdersuites.com"},
  {"name": "Mizunoo", "email": "info@mizunoo.com"},
  {"name": "Gakuto Villas", "email": "bookings@gakutovillas.com"},
  {"name": "Wadano Woods", "email": "bookings@hakubahotelgroup.com"},
  {"name": "Echoland Apartments", "email": "info@echolandapartments.com"},
  {"name": "Iwatake Apartments", "email": "info@iwatakeapartments.com"},
  {"name": "Morino Lodge", "email": "info@morinolodge.com"},
  {"name": "Log Cottage Epoch", "email": "info@hakuba-epoch.com"},
  {"name": "Iwatake Chalet", "email": "bookings@iwatakechalet.com"},
  {"name": "Mominoki Apartments", "email": "info@mominokihotel.com"},
  {"name": "Wadano Hill Chalet", "email": "info@wadanohill.com"}
]

applescript_path = "/tmp/send_emails_now.applescript"

with open(applescript_path, "w", encoding="utf-8") as f:
    f.write('tell application "Mail"\n')
    f.write('activate\n')
    for h in hotels:
        subject = f'Accommodation Inquiry: {h["name"]} - Jan 22 - Jan 30, 2027'
        body = f"""Dear {h['name']} Management,

We are a family of 3 (2 adults, 1 child) planning a ski trip to Hakuba. We would love to stay at your beautiful property!

Check-in: Jan 22, 2027
Check-out: Jan 30, 2027 (8 Nights)
Room Type: Room with Two Double Beds (or a suitable Family Room)

Could you please let me know if you have availability for these dates and what the estimated rate would be?

Thank you so much!
Best regards,
Barry Huang"""
        
        subject_safe = subject.replace('"', '\\"')
        
        body_lines = body.split('\n')
        body_safe_parts = ['"' + line.replace('"', '\\"') + '"' for line in body_lines]
        body_as = ' & return & '.join(body_safe_parts)
        
        f.write(f'    set theMessage to make new outgoing message with properties {{subject:"{subject_safe}", content:({body_as}), visible:false}}\n')
        f.write(f'    tell theMessage to make new to recipient at end of to recipients with properties {{address:"{h["email"]}"}}\n')
        f.write('    send theMessage\n')
        f.write('    delay 0.5\n')
    f.write('end tell\n')

print(f"Executing AppleScript to DIRECTLY SEND {len(hotels)} emails via Mail.app...")
subprocess.run(["osascript", applescript_path])
os.remove(applescript_path)
print("Finished sending all emails!")
