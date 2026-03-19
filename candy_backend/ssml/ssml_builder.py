def build_ssml(text, preset):
    return f"""
<speak version="1.0" xml:lang="de-DE">
  <voice name="de-DE-KatjaNeural">
    <prosody pitch="{preset['pitch']}" rate="{preset['rate']}">
      <mstts:express-as style="{preset['style']}">
        Leo… {text}
      </mstts:express-as>
    </prosody>
  </voice>
</speak>
""".strip()
