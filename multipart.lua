function read_file(path)
  local file, errorMessage = io.open(path, "rb")
  if not file then
      error("Could not read the file:" .. errorMessage .. "\n")
  end

  local content = file:read "*all"
  file:close()
  return content
end

local Boundary = "boundary"
local BodyBoundary = "--" .. Boundary
local LastBoundary = "--" .. Boundary .. "--"
local CRLF = "\r\n"
local FileBody = read_file("random_512x512.png")
local Filename = "random_512x512.png"
local ContentDisposition = 'Content-Disposition: form-data; name="file"; filename="' .. Filename .. '"'
local ContentType = 'Content-Type: image/png'

wrk.method = "POST"
wrk.headers["Content-Type"] = "multipart/form-data; boundary=" .. Boundary
wrk.body = BodyBoundary .. CRLF .. ContentDisposition .. CRLF .. ContentType .. CRLF .. CRLF .. FileBody .. CRLF .. LastBoundary
