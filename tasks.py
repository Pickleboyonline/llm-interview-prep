from invoke import task, Context

@task
def start(c: Context):
    c.run("python -m streamlit run src/app.py")