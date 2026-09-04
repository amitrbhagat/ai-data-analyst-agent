import { useState } from "react";
import Plot from "react-plotly.js";



function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const askQuestion = async () => {
    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setError("");
    setResponse(null);

    try {
      const result = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await result.json();

      if (data.error) {
        setError(data.error);
        return;
      }

      setResponse(data);

    } catch (error) {
      setError(
        "Could not connect to the backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };


  const renderChart = () => {
    if (
      !response ||
      !response.chart_type ||
      response.chart_type === "none" ||
      !response.chart_config
    ) {
      return null;
    }

    const { x, y } = response.chart_config;

    if (response.chart_type === "bar") {
      return (
        <Plot
          data={[
            {
              x: x,
              y: y,
              type: "bar",
            },
          ]}
          layout={{
            title: "Result",
            autosize: true,
          }}
          style={{
            width: "100%",
            height: "400px",
          }}
        />
      );
    }


    if (response.chart_type === "line") {
      return (
        <Plot
          data={[
            {
              x: x,
              y: y,
              type: "scatter",
              mode: "lines+markers",
            },
          ]}
          layout={{
            title: "Result",
            autosize: true,
          }}
          style={{
            width: "100%",
            height: "400px",
          }}
        />
      );
    }

    return null;
  };


  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >

      <h1>AI Data Analyst</h1>

      <p>
        Ask questions about your business data or company policies.
      </p>


      {/* Question Input */}

      <div
        style={{
          display: "flex",
          gap: "10px",
        }}
      >

        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
          placeholder="Ask a question..."
          style={{
            flex: 1,
            padding: "12px",
            fontSize: "16px",
          }}
        />

        <button
          onClick={askQuestion}
          disabled={loading}
          style={{
            padding: "12px 20px",
            fontSize: "16px",
          }}
        >
          {loading ? "Analyzing..." : "Ask"}
        </button>

      </div>


      {/* Error */}

      {error && (
        <div style={{ marginTop: "20px" }}>
          <strong>Error:</strong>
          <p>{error}</p>
        </div>
      )}


      {/* Response */}

      {response && (
        <div style={{ marginTop: "30px" }}>

          {/* Answer */}

          <h2>Answer</h2>

          <p>
            {response.final_answer}
          </p>


          {/* SQL */}

          {response.generated_sql && (
            <>
              <h2>SQL Query</h2>

              <pre
                style={{
                  background: "#f4f4f4",
                  padding: "15px",
                  overflowX: "auto",
                }}
              >
                {response.generated_sql}
              </pre>
            </>
          )}


          {/* Data Table */}

          {response.query_result &&
            response.query_result.length > 0 && (
              <>
                <h2>Data</h2>

                <div style={{ overflowX: "auto" }}>

                  <table
                    border="1"
                    cellPadding="8"
                    style={{
                      borderCollapse: "collapse",
                      width: "100%",
                    }}
                  >

                    <thead>
                      <tr>
                        {Object.keys(response.query_result[0]).map(
                          (column) => (
                            <th key={column}>
                              {column}
                            </th>
                          )
                        )}
                      </tr>
                    </thead>


                    <tbody>

                      {response.query_result.map(
                        (row, rowIndex) => (
                          <tr key={rowIndex}>

                            {Object.keys(
                              response.query_result[0]
                            ).map((column) => (
                              <td key={column}>
                                {String(row[column])}
                              </td>
                            ))}

                          </tr>
                        )
                      )}

                    </tbody>

                  </table>

                </div>
              </>
            )}


          {/* Chart */}

          {response.chart_type &&
            response.chart_type !== "none" && (
              <>
                <h2>Chart</h2>

                {renderChart()}
              </>
            )}


          {/* Sources */}

          {response.sources &&
            response.sources.length > 0 && (
              <>
                <h2>Sources</h2>

                <ul>
                  {response.sources.map(
                    (source, index) => (
                      <li key={index}>
                        {source}
                      </li>
                    )
                  )}
                </ul>
              </>
            )}

        </div>
      )}

    </div>
  );
}


export default App;
