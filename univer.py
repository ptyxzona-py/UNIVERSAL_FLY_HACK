-- Demo UI (safe, local-only) for learning Roblox Lua
-- IMPORTANT: This script is a UI-only demo. It does NOT modify the player's character, movement, collisions,
-- or affect other players or the server. I WILL NOT provide real bypass/cheat functionality.
-- Paste this LocalScript into StarterPlayer > StarterPlayerScripts in Roblox Studio.

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Create ScreenGui
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "DemoClientGui"
screenGui.ResetOnSpawn = false
screenGui.Parent = playerGui

-- Main panel
local panel = Instance.new("Frame")
panel.Name = "Panel"
panel.Size = UDim2.new(0, 420, 0, 200)
panel.Position = UDim2.new(0, 16, 0, 80)
panel.BackgroundColor3 = Color3.fromRGB(28, 28, 30)
panel.BorderSizePixel = 0
panel.Parent = screenGui

local title = Instance.new("TextLabel")
title.Name = "Title"
title.Size = UDim2.new(1, -12, 0, 28)
title.Position = UDim2.new(0, 6, 0, 6)
title.BackgroundTransparency = 1
title.Text = "Safe Demo UI"
title.TextColor3 = Color3.fromRGB(235, 235, 235)
title.Font = Enum.Font.SourceSansSemibold
title.TextSize = 18
title.TextXAlignment = Enum.TextXAlignment.Left
title.Parent = panel

-- Demo avatar icon (visual only)
local avatar = Instance.new("ImageLabel")
avatar.Name = "Avatar"
avatar.Size = UDim2.new(0, 72, 0, 72)
avatar.Position = UDim2.new(0, 10, 0, 44)
avatar.BackgroundTransparency = 1
avatar.Image = "rbxasset://textures/ui/GuiImagePlaceholder.png" -- placeholder image
avatar.Parent = panel

local avatarLabel = Instance.new("TextLabel")
avatarLabel.Size = UDim2.new(1, -160, 0, 72)
avatarLabel.Position = UDim2.new(0, 94, 0, 44)
avatarLabel.BackgroundTransparency = 1
avatarLabel.Text = "Client-side demo avatar\n(doesn't affect gameplay)"
avatarLabel.TextColor3 = Color3.fromRGB(200, 200, 200)
avatarLabel.Font = Enum.Font.SourceSans
avatarLabel.TextSize = 14
avatarLabel.TextXAlignment = Enum.TextXAlignment.Left
avatarLabel.TextYAlignment = Enum.TextYAlignment.Top
avatarLabel.Parent = panel

-- Fake wall for noclip demonstration (UI only)
local fakeWall = Instance.new("Frame")
fakeWall.Name = "FakeWall"
fakeWall.Size = UDim2.new(0, 12, 0, 80)
fakeWall.Position = UDim2.new(0, 60, 0, 46)
fakeWall.BackgroundColor3 = Color3.fromRGB(120, 120, 120)
fakeWall.BorderSizePixel = 0
fakeWall.BackgroundTransparency = 0.4
fakeWall.Visible = true
fakeWall.Parent = panel

-- Status label
local statusLabel = Instance.new("TextLabel")
statusLabel.Name = "Status"
statusLabel.Size = UDim2.new(1, -12, 0, 20)
statusLabel.Position = UDim2.new(0, 6, 1, -38)
statusLabel.BackgroundTransparency = 1
statusLabel.Text = "Status: Idle (Demo)"
statusLabel.TextColor3 = Color3.fromRGB(180, 180, 180)
statusLabel.Font = Enum.Font.SourceSans
statusLabel.TextSize = 14
statusLabel.TextXAlignment = Enum.TextXAlignment.Left
statusLabel.Parent = panel

-- Note label (includes requested text)
local noteLabel = Instance.new("TextLabel")
noteLabel.Name = "Note"
noteLabel.Size = UDim2.new(1, -12, 0, 28)
noteLabel.Position = UDim2.new(0, 6, 1, -10)
noteLabel.BackgroundTransparency = 1
noteLabel.Text = "Note: If you got banned, the creator has no responsibility for the ban, USE THIS AS YOUR OWN RISK!"
noteLabel.TextColor3 = Color3.fromRGB(210, 160, 160)
noteLabel.Font = Enum.Font.SourceSansBold
noteLabel.TextSize = 12
noteLabel.TextXAlignment = Enum.TextXAlignment.Left
noteLabel.TextYAlignment = Enum.TextYAlignment.Center
noteLabel.Parent = panel

-- Helper to create buttons
local function makeButton(name, text, posX, posY)
	local btn = Instance.new("TextButton")
	btn.Name = name
	btn.Size = UDim2.new(0, 110, 0, 32)
	btn.Position = UDim2.new(0, posX, 0, posY)
	btn.AnchorPoint = Vector2.new(0, 0)
	btn.BackgroundColor3 = Color3.fromRGB(50, 50, 55)
	btn.BorderSizePixel = 0
	btn.Text = text
	btn.TextColor3 = Color3.fromRGB(235, 235, 235)
	btn.Font = Enum.Font.SourceSansSemibold
	btn.TextSize = 14
	btn.Parent = panel
	return btn
end

local flyBtn = makeButton("FlyBtn", "Fly (Demo)", 182, 44)
local noclipBtn = makeButton("NoclipBtn", "Noclip (Demo)", 182, 80)
local killBtn = makeButton("KillBtn", "Kill (Demo)", 182, 116)
local bypassBtn = makeButton("BypassBtn", "Bypasser (Demo)", 306, 44) -- demo-only bypass button

-- Demo state
local isFlying = false
local isNoclipping = false
local isKilled = false
local isBypassing = false

-- Layout baseline
local baseAvatarPos = avatar.Position
local t = 0

-- Helper visual effects (UI-only)
local function setStatus(text, color)
	statusLabel.Text = "Status: " .. text .. " (Demo)"
	statusLabel.TextColor3 = color or Color3.fromRGB(180, 180, 180)
end

flyBtn.MouseButton1Click:Connect(function()
	if isKilled then
		isKilled = false
		avatar.ImageColor3 = Color3.fromRGB(255,255,255)
		avatar.ImageTransparency = 0
		avatarLabel.TextColor3 = Color3.fromRGB(200,200,200)
	end
	isFlying = not isFlying
	isNoclipping = false
	isBypassing = false
	flyBtn.Text = (isFlying and "Stop Fly (Demo)" or "Fly (Demo)")
	noclipBtn.Text = "Noclip (Demo)"
	bypassBtn.Text = "Bypasser (Demo)"
	setStatus(isFlying and "Flying (UI demo)" or "Idle", isFlying and Color3.fromRGB(120, 220, 255) or nil)
	fakeWall.Visible = not isNoclipping
	if not isFlying then
		avatar.Position = baseAvatarPos
		avatar.Size = UDim2.new(0,72,0,72)
	end
end)

noclipBtn.MouseButton1Click:Connect(function()
	if isKilled then
		isKilled = false
		avatar.ImageColor3 = Color3.fromRGB(255,255,255)
		avatar.ImageTransparency = 0
		avatarLabel.TextColor3 = Color3.fromRGB(200,200,200)
	end
	isNoclipping = not isNoclipping
	isFlying = false
	isBypassing = false
	noclipBtn.Text = (isNoclipping and "Stop Noclip (Demo)" or "Noclip (Demo)")
	flyBtn.Text = "Fly (Demo)"
	bypassBtn.Text = "Bypasser (Demo)"
	setStatus(isNoclipping and "Noclipping (UI demo)" or "Idle", isNoclipping and Color3.fromRGB(180,180,120) or nil)
	fakeWall.Visible = not isNoclipping
	avatar.Position = baseAvatarPos
	avatar.Size = UDim2.new(0,72,0,72)
end)

killBtn.MouseButton1Click:Connect(function()
	isKilled = not isKilled
	isFlying = false
	isNoclipping = false
	isBypassing = false
	flyBtn.Text = "Fly (Demo)"
	noclipBtn.Text = "Noclip (Demo)"
	bypassBtn.Text = "Bypasser (Demo)"
	fakeWall.Visible = true

	if isKilled then
		avatar.ImageColor3 = Color3.fromRGB(180, 30, 30)
		avatar.ImageTransparency = 0.15
		avatarLabel.TextColor3 = Color3.fromRGB(180, 30, 30)
		setStatus("Killed (UI demo)", Color3.fromRGB(200,60,60))
		local flash = Instance.new("Frame")
		flash.Name = "Flash"
		flash.Size = UDim2.new(1,0,1,0)
		flash.Position = UDim2.new(0,0,0,0)
		flash.BackgroundColor3 = Color3.fromRGB(255, 60, 60)
		flash.BackgroundTransparency = 0.8
		flash.ZIndex = 10
		flash.Parent = panel
		coroutine.wrap(function()
			for i = 1, 6 do
				flash.BackgroundTransparency = 0.5 + i * 0.08
				wait(0.06)
			end
			flash:Destroy()
		end)()
	else
		avatar.ImageColor3 = Color3.fromRGB(255,255,255)
		avatar.ImageTransparency = 0
		avatarLabel.TextColor3 = Color3.fromRGB(200,200,200)
		setStatus("Idle")
	end
end)

bypassBtn.MouseButton1Click:Connect(function()
	-- REFUSAL: This does NOT perform any real bypass. It is only a local UI visual effect for demo/educational purposes.
	-- Toggle UI-only "bypass" visual
	isBypassing = not isBypassing
	if isBypassing then
		-- stop other demos for clarity
		isFlying = false
		isNoclipping = false
		isKilled = false
		flyBtn.Text = "Fly (Demo)"
		noclipBtn.Text = "Noclip (Demo)"
		killBtn.Text = "Kill (Demo)"
		bypassBtn.Text = "Stop Bypasser (Demo)"
		setStatus("Bypasser active (UI demo)", Color3.fromRGB(170,130,255))
		-- subtle visual cue
		avatarLabel.TextColor3 = Color3.fromRGB(170,130,255)
		avatar.ImageTransparency = 0.05
	else
		bypassBtn.Text = "Bypasser (Demo)"
		setStatus("Idle")
		avatarLabel.TextColor3 = Color3.fromRGB(200,200,200)
		avatar.ImageTransparency = 0
	end
end)

-- Animate loop (client-only visual)
local conn
conn = RunService.RenderStepped:Connect(function(dt)
	t = t + dt
	if isBypassing then
		-- Glitchy color pulse (UI-only)
		local pulse = (math.sin(t * 12) + 1) / 2 -- 0..1
		local r = 170 + pulse * 85
		local g = 130 + pulse * 40
		local b = 255
		avatar.ImageColor3 = Color3.fromRGB(math.clamp(r,0,255), math.clamp(g,0,255), b)
		-- small jitter position
		local jx = math.sin(t * 40) * 2
		local jy = math.cos(t * 33) * 2
		avatar.Position = UDim2.new(baseAvatarPos.X.Scale, baseAvatarPos.X.Offset + jx,
			baseAvatarPos.Y.Scale, baseAvatarPos.Y.Offset + jy)
		avatar.Size = UDim2.new(0, 74, 0, 74)
	elseif isFlying then
		local dy = math.sin(t * 3) * -16
		avatar.Position = UDim2.new(baseAvatarPos.X.Scale, baseAvatarPos.X.Offset,
			baseAvatarPos.Y.Scale, baseAvatarPos.Y.Offset + dy)
		local scale = 1 + (math.sin(t * 6) * 0.03)
		avatar.Size = UDim2.new(0, 72 * scale, 0, 72 * scale)
	elseif isNoclipping then
		local speed = 48
		local offsetX = (t * speed) % 160
		avatar.Position = UDim2.new(baseAvatarPos.X.Scale, baseAvatarPos.X.Offset + offsetX - 40,
			baseAvatarPos.Y.Scale, baseAvatarPos.Y.Offset)
		avatar.Size = UDim2.new(0, 72, 0, 72)
	else
		-- idle
		local dy = math.sin(t * 1.2) * -2
		avatar.Position = UDim2.new(baseAvatarPos.X.Scale, baseAvatarPos.X.Offset,
			baseAvatarPos.Y.Scale, baseAvatarPos.Y.Offset + dy)
		avatar.Size = UDim2.new(0, 72, 0, 72)
		avatar.ImageColor3 = Color3.fromRGB(255,255,255)
	end
end)

-- Clean up if the player leaves or script is removed
player.AncestryChanged:Connect(function()
	if not player:IsDescendantOf(game) and conn then
		conn:Disconnect()
	end
end)
