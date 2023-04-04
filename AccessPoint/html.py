def getConfigureHtml():
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="refresh" content="1; url='http://192.168.4.1'" />
    <title>Document</title>
    <style>
      body {
        background-color: #1e212a;
        color: #f9fafb;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2>Saved!</h2>
  </body>
</html>"""

def getConnectedHtml(ssid):
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        background-color: #1e212a;
        color: #f9fafb;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2>Successfully connected to Wifi: %s</h2>
  </body>
</html>"""%(ssid)

def getConnectionFailedHtml(ssid):
     return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      body {
        background-color: #1e212a;
        color: #f9fafb;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2>Failed to connect to Wifi: %s</h2>
  </body>
</html>"""%(ssid)




def getRootHtml(ssids,profiles):

    ssid = list(profiles.keys())[0]
    password = profiles[ssid]

    before = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      console.log(axios);
    </script>
    <style>
      .flex-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      body {
        background-color: #1e212a;
        color: #f9fafb;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
      }
      #pw-input {
        margin-left:5px;
      }

      p {
        display: block;
        margin-block-start: 0.5em;
        margin-block-end: 0.5em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;
      }

      h3 {
        color: #8686e1;
      }
    #frame {
        border-radius: 2px;
        background-color: #8686e1;
      }

      #input-wrapper {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
      }
      .input-button {
        border-radius: 16px;
        border-width: 0px;
        margin-top: 10px;
        padding: 10px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <body>
      <div class="flex-box">
        <h2>Access Point Dashboard</h2>
        <div class="flex-box">
          <h3>Sensors:</h3>
          <p>Temperature: 20 F</p>
          <p>Humidity: 50%%</p>
        </div>
        <div class="flex-box">
          <form class="flex-box" action="configure" method="post">
            <h3 style="margin-top: 50px">Wifi Credentails:</h3>
            <p>SSID:</p>
            <input id="ssid-input" name="ssid" value="%s" />

            <p onClick="showNetworks()" style="cursor: pointer;">
              <svg
                id="svg"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 1000 1000"
                enable-background="new 0 0 1000 1000"
                xml:space="preserve"
                width="10px"
                height="10px"
                fill="white"
                style="cursor: pointer"
              >
                <g>
                  <path
                    d="M500,713.3L10,390.4l68.5-103.8L500,564.5l421.5-277.9L990,390.4L500,713.3z"
                  />
                </g>
              </svg>
              show available networks
            </p>"""%(ssid)


    after = """
              <p style="margin-top: 20px">Password:</p>
              <div id="input-wrapper">
              <input
                id="pw-input"
                name="password"
                type="password"
                value="%s"
              /><span
                style="margin-left: 5px"
                id="show-span"
                onclick="toggleInput()"
                ><svg
                  width="20px"
                  fill="white"
                  height="20px"
                  viewBox="0 0 48 48"
                  xmlns="http://www.w3.org/2000/svg"
                  style="cursor: pointer"
                >
                  <path d="M0 0h48v48H0z" fill="none" />
                  <g id="Shopicon">
                    <path
                      d="M24,38c12,0,20-14,20-14s-8-14-20-14S4,24,4,24S12,38,24,38z M24,14c7.072,0,12.741,6.584,15.201,9.992
                      C36.728,27.396,31.024,34,24,34c-7.072,0-12.741-6.584-15.201-9.992C11.272,20.604,16.976,14,24,14z"
                    />
                    <path
                      d="M24,32c4.418,0,8-3.582,8-8s-3.582-8-8-8s-8,3.582-8,8S19.582,32,24,32z M24,20c2.206,0,4,1.794,4,4c0,2.206-1.794,4-4,4
                      s-4-1.794-4-4C20,21.794,21.794,20,24,20z"
                    />
                  </g></svg
              ></span>
            </div>
             <input
              class="input-button"
              style="margin-top: 50px"
              type="submit"
              value="Save Credentials"
            />
          </form>
          <form action="connect" method="get">
            <p style="text-align: center; color: blue">
              <input
                class="input-button"
                type="submit"
                value="Connect to Wifi"
              />
            </p>
          </form>
        </div>
      </div>
      <script>
        function toggleInput() {
          const input = document.getElementById("pw-input");
          const show = document.getElementById("show-span");

          const hideSvg = `<svg
                  width="20px"
                  height="20px"
                  viewBox="0 0 48 48"
                  fill="white"
                  xmlns="http://www.w3.org/2000/svg"
                  style="cursor: pointer"
                >
                  <path d="M0 0h48v48H0z" fill="none" />
                  <g id="Shopicon">
                    <path
                      d="M11.957,33.215L7.172,38L10,40.828l5.305-5.305C17.867,36.992,20.788,38,24,38c12,0,20-14,20-14s-2.954-5.16-7.957-9.215
                      L40.828,10L38,7.172l-5.305,5.305C30.133,11.008,27.212,10,24,10C12,10,4,24,4,24S6.954,29.16,11.957,33.215z M33.204,17.624
                      c2.668,2.091,4.747,4.638,5.996,6.369C36.728,27.396,31.024,34,24,34c-2.048,0-3.973-0.563-5.742-1.43l1.684-1.684
                      C21.133,31.589,22.517,32,24,32c4.418,0,8-3.582,8-8c0-1.483-0.411-2.867-1.114-4.058L33.204,17.624z M20.149,25.023
                      C20.062,24.694,20,24.356,20,24c0-2.206,1.794-4,4-4c0.356,0,0.694,0.062,1.023,0.149L20.149,25.023z M27.851,22.977
                      C27.938,23.306,28,23.644,28,24c0,2.206-1.794,4-4,4c-0.356,0-0.694-0.062-1.023-0.149L27.851,22.977z M24,14
                      c2.048,0,3.973,0.563,5.742,1.43l-1.684,1.684C26.867,16.411,25.483,16,24,16c-4.418,0-8,3.582-8,8
                      c0,1.483,0.411,2.867,1.114,4.058l-2.318,2.318c-2.668-2.091-4.747-4.638-5.997-6.369C11.272,20.604,16.976,14,24,14z"
                    />
                  </g></svg
              >`;

          const showSvg = `<svg style="cursor: pointer" width="20px" fill="white" height="20px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" >

<path d="M0 0h48v48H0z" fill="none"/>
<g id="Shopicon">
	<path d="M24,38c12,0,20-14,20-14s-8-14-20-14S4,24,4,24S12,38,24,38z M24,14c7.072,0,12.741,6.584,15.201,9.992
		C36.728,27.396,31.024,34,24,34c-7.072,0-12.741-6.584-15.201-9.992C11.272,20.604,16.976,14,24,14z"/>
	<path d="M24,32c4.418,0,8-3.582,8-8s-3.582-8-8-8s-8,3.582-8,8S19.582,32,24,32z M24,20c2.206,0,4,1.794,4,4c0,2.206-1.794,4-4,4
		s-4-1.794-4-4C20,21.794,21.794,20,24,20z"/>
</g>
</svg>`;
          if (input.type === "password") {
            input.type = "text";
            show.innerHTML = hideSvg;
          } else {
            input.type = "password";
            show.innerHTML = showSvg;
          }
        }
        function showNetworks() {
          const list = document.getElementById("wifi-list");
          const svg = document.getElementById("svg");

          if (list.style.display !== "none") {
            list.style.display = "none";
            svg.setAttribute("transform", "rotate(0)");
            //console.log(list.style);
            //show.innerText = "hide";
          } else {
            list.style.display = "block";
            svg.setAttribute("transform", "rotate(180)");
            /* input.type = "password";
            show.innerText = "show"; */
          }
          console.log(list.style);
        }
        function setSSID(newSSID) {
          const ssid = document.getElementById("ssid-input");
          ssid.value = newSSID;
        }
      </script>
    </body>
  </body>
</html>
    """%(password)

    wifiHtml = """<div id="wifi-list" style="display: none; width: 60%;">"""

    while len(ssids):
            ssid = ssids.pop(0)
            wifiHtml += f"""<p onClick="setSSID('{ssid}')" style="cursor: pointer;">{ssid}</p>"""

    wifiHtml += """</div>"""

    final = before+wifiHtml+after
    return final

                        

""" f = open("output/index.html", "w")
f.write(getRootHtml(["one twooooooooooooooooo","two","three"],{'testname':'testpw'}))
#f.write(getConnectionFailedHtml("my test Wifi name"))
f.close() """