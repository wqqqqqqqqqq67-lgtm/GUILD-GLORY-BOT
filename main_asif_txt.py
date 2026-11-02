{
  "version": 2,
  "builds": [
    {
      "src": "main_asif_txt.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main_asif_txt.py"
    }
  ]
}
