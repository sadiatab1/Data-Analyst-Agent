from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from handler import process_question  # Make sure this is NOT commented

app = FastAPI(
    title="Data Analyst Agent API",
    description="An API that accepts a data analysis task and returns answers with visualizations.",
    version="1.0.0"
)

@app.post("/api/")
async def analyze(file: UploadFile = File(...)):
    """
    Accepts a text file describing a data analysis task.
    Returns the result as JSON (answers + base64-encoded plot if needed).
    """
    try:
        content = await file.read()
        task_description = content.decode()

        result = process_question(task_description)

        # If it's an error, return as is
        if isinstance(result, dict) and "error" in result:
            return JSONResponse(content=result, status_code=500)

        # Format the structured response
        response = {
            "answer_1": result[0],
            "answer_2": result[1],
            "answer_3": result[2],
            "scatterplot": result[3],
            "additional_graphs": result[4]  # this is a dict with 4 base64-encoded graphs
        }

        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
    

