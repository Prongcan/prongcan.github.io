---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

<strong style="font-size: 1.4em;">Towards Data-Efficient and Trustworthy Reasoning.</strong>

I am an undergraduate student at **Tongji University**, advised by Prof. **Miaomiao Zhang**.

Since April 2025, I have been a visiting student at **Westlake University**, advised Prof. [**Yue Zhang**](https://frcchang.github.io/). I also work closely with Prof. [**Qi Zhu**](https://gentlezhu.github.io/) at **Zhejiang University**, where I am researching the attention mechanisms of Vision-Language Models and working to enhance their long-context reasoning abilities. 
Since April 2026, I have been a research intern at the **University of Virginia**, advised by Prof. [**Yu Meng**](https://yumeng5.github.io/). My research focuses on post-training of LLM.

# 🔥 News
<div class="phd-opportunity">📌 Pinned: I am looking for PhD opportunities for Fall 2027!</div>

- *2026.09*: &nbsp;🎉 I'm excited to join **Ant Group** as an **AI Researcher (Intern)**!
- *2026.09*: &nbsp;🚀 We propose [**NSD**](https://arxiv.org/pdf/2609.11699), our new work on improving LLM reasoning through negative self-distillation!
- *2026.08*: &nbsp;🌍✈️ Attended **IJCAI 2026** in beautiful **Bremen, Germany**!
- *2026.07*: &nbsp;🎉 Our paper "DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation" has been accepted by **COLM 2026 Workshop LM4Sci**!
- *2026.05*: &nbsp;🎉 Our paper "VERA: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding" has been accepted by **IJCAI 2026**!
- *2026.04*: &nbsp;🎉 Our paper "Augmenting Multi-Technique Static Analysis with Large Language Models" has been accepted by **ISSTA 2026**!

<style>
.phd-opportunity {
  display: inline-block;
  margin: 0.15rem 0 0.65rem;
  color: #1261c9;
  background: linear-gradient(105deg, #edf6ff 0%, #f5f9ff 100%);
  border: 1px solid #c9e0ff;
  border-left: 4px solid #2684ff;
  border-radius: 8px;
  box-shadow: 0 4px 14px rgba(30, 105, 205, 0.09);
  padding: 0.5rem 0.8rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
#experience-list {
  list-style: none;
  margin: 0;
  padding: 0;
}
#experience-list li {
  display: grid;
  grid-template-columns: 92px minmax(0, 1fr);
  align-items: center;
  gap: 12px;
  min-height: 54px;
  margin: 0 0 12px;
}
#experience-list img {
  display: block;
  width: 48px;
  height: 48px;
  object-fit: contain;
}
#experience-list img.experience-logo-wide {
  width: 90px;
  height: auto;
}
#experience-list img.experience-logo-westlake {
  width: 42px;
  height: 42px;
}
#experience-list img.experience-logo-zju {
  width: 76px;
  height: 62px;
  transform: translateX(-15px);
}
.experience-tree-section {
  position: relative;
  margin: 2.4rem 0 2.7rem;
}
.experience-tree-header {
  position: relative;
  padding: 0;
}
.experience-tree-title {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin: 0 0 0.55rem;
  border: 0;
  color: #173a5e;
  font-size: 1.55rem;
  line-height: 1.2;
}
.experience-tree-title::before {
  display: none;
}
.experience-tree-title-icon {
  display: inline-grid;
  place-items: center;
  width: 2.15rem;
  height: 2.15rem;
  flex: 0 0 2.15rem;
  border-radius: 12px;
  color: #fff;
  background: linear-gradient(135deg, #3178e0, #26a69a);
  box-shadow: 0 6px 16px rgba(49, 120, 224, 0.23);
  font-size: 1.05rem;
}
.experience-tree-description {
  max-width: 720px;
  margin: 0;
  color: #5d7187;
  font-size: 0.92rem;
  line-height: 1.65;
}
#experience-tree-container {
  width: 100%;
  overflow-x: auto;
  margin: 0;
  padding: 0.2rem 0 0.65rem;
  scrollbar-color: #a9c7e8 transparent;
  scrollbar-width: thin;
}
#experience-tree {
  width: 100%;
  min-height: 0;
  display: block;
}
#experience-tree .node-rect {
  transition: filter 0.25s ease, opacity 0.25s ease, stroke 0.25s ease;
}
#experience-tree .node-text {
  font-family: "Trebuchet MS", Helvetica, sans-serif;
  pointer-events: none;
  user-select: none;
}
@keyframes float1 {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-2px); }
}
@keyframes float2 {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-1.5px); }
}
@keyframes nodeGrowIn {
  0% {
    opacity: 0;
    transform: translateX(-16px) scale(0.36);
  }
  58% {
    opacity: 1;
    transform: translateX(2px) scale(1.055);
  }
  78% {
    transform: translateX(-1px) scale(0.985);
  }
  100% {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}
@keyframes branchGrow {
  from { stroke-dashoffset: var(--branch-length); }
  to { stroke-dashoffset: 0; }
}
@keyframes budPulse {
  0% { opacity: 0; transform: scale(0.2); }
  55% { opacity: 1; transform: scale(1.35); }
  100% { opacity: 0.85; transform: scale(1); }
}
.tree-node-inner {
  transform-box: fill-box;
  transform-origin: left center;
}
.tree-branch {
  animation-fill-mode: both;
  animation-timing-function: cubic-bezier(0.34, 0.08, 0.28, 1);
}
.tree-bud {
  transform-box: fill-box;
  transform-origin: center;
}
.tree-click-effect {
  pointer-events: none;
}
.tree-node:focus {
  outline: none;
}
.tree-node:focus .node-rect {
  stroke: #175fc1;
  stroke-width: 2.5px;
}
@media (prefers-reduced-motion: reduce) {
  .tree-node-inner,
  .tree-branch,
  .tree-bud {
    animation: none !important;
    opacity: 1 !important;
  }
}
.tree-popover {
  position: fixed;
  background: rgba(255, 255, 255, 0.97);
  border: 1px solid #c9ddf2;
  border-radius: 12px;
  padding: 14px 17px 15px;
  max-width: 380px;
  box-shadow: 0 14px 36px rgba(24, 65, 108, 0.18);
  z-index: 9999;
  display: none;
  font-family: "Trebuchet MS", Helvetica, sans-serif;
  pointer-events: none;
}
.tree-popover-title {
  font-weight: bold;
  color: #2268bd;
  font-size: 14px;
  margin-bottom: 6px;
}
.tree-popover-body {
  color: #555;
  font-size: 13px;
  line-height: 1.65;
}
@media (max-width: 600px) {
  .experience-tree-title { font-size: 1.4rem; }
}
</style>

<section class="experience-tree-section" aria-labelledby="experience-tree-title">
  <header class="experience-tree-header">
    <h1 class="experience-tree-title" id="experience-tree-title"><span class="experience-tree-title-icon" aria-hidden="true">✶</span> My Experience Tree</h1>
    <p class="experience-tree-description">I am committed to comprehensively understanding and researching the full pipeline of LLM training and inference. This map connects the questions, methods, and applications that shape my research.</p>
  </header>
  <div id="experience-tree-container">
    <svg id="experience-tree" role="img" aria-label="Interactive map of research experience"></svg>
  </div>
</section>
<div class="tree-popover" id="tree-popover" role="tooltip">
  <div class="tree-popover-title" id="tree-popover-title"></div>
  <div class="tree-popover-body" id="tree-popover-body"></div>
</div>

<script>
(function() {
  // ============================================================
  // EXPERIENCE TREE DATA — edit the content below as you like
  // ============================================================
  var treeData = {
    name: "My Research",
    details: "Overview of my research.",
    children: [
      {
        name: "V/LLM Attention Study",
        details: "In VERA, we analyze the attention mechanism of VLM when processing long visual documents. We find a small set of attention heads with surprising retrieval ability. This motivates us to regard them as a natural retriever and integrate this RAG process into the inference.",
        children: [
          { name: "Inference Optimization", details: "In VERA, we integrate retrieval augmentation into the reasoning process by adjusting the KV cache. After retrieving evidence, rather than discarding the KV cache and re-running inference, we retain the KV cache and complete the remaining prefill of the retrieved evidence. This insprie me to explore more ideas on this direction!" }
        ]
      },
      {
        name: "Reasoning & Augmentation",
        details: "Reasoning performance can be enhanced by both RAG (VERA and DeepInstructor) and post-training (NSD).",
        children: [
          { name: "Post Training", appearance: "branch", details: "Negative Self-Distillation (NSD) shows that self-improvement can come from learning which reasoning behaviors to avoid. A teacher conditioned on correct answers can encourage overconfidence and weaken self-correction. We construct a negative teacher from the model itself, then use dynamic token-level gating to target reasoning flaws while preserving basic language abilities. The key insight is that selective negative feedback can improve reasoning without ground-truth answers or an external teacher, while retaining exploration and self-correction." },
          { name: "Agent & RAG", details: "We develop DeepInstructor, which transforms OpenReview data into a graph database with a dedicated retriever to enhance the agent's idea evaluation capability. VERA explores RAG-based reasoning enhancement from an attention-level perspective.", children: [
            { name: "AI for Research and Safety", details: "DeepInstructor and ELSA address research ideation and smart contract vulnerability detection, respectively. Through these projects, I learned how to define real-world problems where AI can provide meaningful solutions, and how to collect and process domain-specific data." }
          ] }
        ]
      }
    ]
  };

  // ============================================================
  // RENDERING — horizontal pipeline tree
  // ============================================================
  var container = document.getElementById('experience-tree-container');
  var svg = document.getElementById('experience-tree');
  var popover = document.getElementById('tree-popover');
  var popoverTitle = document.getElementById('tree-popover-title');
  var popoverBody = document.getElementById('tree-popover-body');

  var levelSpacing = 260;
  var marginX = 50;
  var marginTop = 4;
  var marginBot = 4;
  var nodeH = 50;
  var leafH = 42;
  var textPad = 26;
  var siblingGap = 12;

  function textWidth(text, fs) {
    fs = fs || 11;
    var w = 0;
    for (var i = 0; i < text.length; i++) {
      var c = text.charCodeAt(i);
      if (c > 127) w += fs * 0.88; else w += fs * 0.57;
    }
    return w + textPad * 2;
  }

  function computeLayout(node) {
    if (!node.children || node.children.length === 0) { node._h = 1; return; }
    var h = 0;
    for (var i = 0; i < node.children.length; i++) { computeLayout(node.children[i]); h += node.children[i]._h; }
    node._h = Math.max(h, 1);
  }

  function assignPositions(node, depth, top, bottom) {
    node._depth = depth;
    node._y = (top + bottom) / 2;
    node._x = marginX + depth * levelSpacing;
    if (node.children && node.children.length > 0) {
      var t = top, u = (bottom - top) / node._h;
      for (var i = 0; i < node.children.length; i++) {
        var b = t + node.children[i]._h * u;
        assignPositions(node.children[i], depth + 1, t, b);
        t = b;
      }
    }
  }

  function getMaxDepth(node, d) {
    d = d || 0;
    if (!node.children || node.children.length === 0) return d;
    var m = d;
    for (var i = 0; i < node.children.length; i++) m = Math.max(m, getMaxDepth(node.children[i], d + 1));
    return m;
  }

  function collectNodes(node, arr) {
    arr.push(node);
    if (node.children) for (var i = 0; i < node.children.length; i++) collectNodes(node.children[i], arr);
  }

  function assignGrowthOrder(root) {
    var queue = [root];
    var order = 0;
    while (queue.length) {
      var current = queue.shift();
      current._growOrder = order++;
      if (current.children) {
        for (var i = 0; i < current.children.length; i++) queue.push(current.children[i]);
      }
    }
  }

  var introHasPlayed = false;
  var introInProgress = false;
  var resizeQueuedDuringIntro = false;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function render() {
    var shouldAnimateIntro = !introHasPlayed && !reduceMotion;
    var cw = Math.max(container.clientWidth - 20, 750);
    computeLayout(treeData);
    assignGrowthOrder(treeData);
    var totalH = Math.max(treeData._h * (leafH + siblingGap) + marginTop + marginBot, 220);
    assignPositions(treeData, 0, marginTop, totalH - marginBot);

    // Compute centering offset
    var nodes = [];
    collectNodes(treeData, nodes);
    var minX = Infinity, maxX = -Infinity;
    for (var i = 0; i < nodes.length; i++) {
      var nd = nodes[i];
      nd._isLeaf = (!nd.children || nd.children.length === 0) && nd.appearance !== 'branch';
      nd._isRoot = (nd === treeData);
      nd._w = textWidth(nd.name, nd._isLeaf ? 11.3 : (nd._isRoot ? 13.2 : 12.2)) + (nd._isLeaf ? 20 : 24);
      nd._hp = nd._isLeaf ? leafH : (nd._isRoot ? 54 : nodeH);
      if (nd._x - nd._w/2 < minX) minX = nd._x - nd._w/2;
      if (nd._x + nd._w/2 > maxX) maxX = nd._x + nd._w/2;
    }
    var treeWidth = maxX - minX;
    var offsetX = (cw - treeWidth) / 2 - minX;
    var horizontalSafeArea = 42;
    if (offsetX + minX < horizontalSafeArea) {
      offsetX = horizontalSafeArea - minX;
    }

    // Apply centering offset
    for (var i = 0; i < nodes.length; i++) {
      nodes[i]._x += offsetX;
    }

    var maxD = getMaxDepth(treeData);
    var totalW = Math.max(cw, offsetX + maxX + marginX);

    // Recompute min/max after shift
    var newMinY = Infinity, newMaxY = -Infinity;
    for (var i = 0; i < nodes.length; i++) {
      if (nodes[i]._y - nodes[i]._hp/2 < newMinY) newMinY = nodes[i]._y - nodes[i]._hp/2;
      if (nodes[i]._y + nodes[i]._hp/2 > newMaxY) newMaxY = nodes[i]._y + nodes[i]._hp/2;
    }
    totalH = Math.max(newMaxY + marginBot, 220);

    svg.setAttribute('viewBox', '0 0 ' + totalW + ' ' + totalH);
    var availableW = container.clientWidth;
    var displayScale = Math.min(1, Math.max(0.62, availableW / totalW));
    var displayW = Math.max(availableW, totalW * displayScale);
    var displayH = totalH * displayScale;
    svg.setAttribute('width', displayW);
    svg.setAttribute('height', displayH);
    svg.style.width = displayW + 'px';
    svg.style.height = displayH + 'px';
    svg.innerHTML = '';

    // Defs
    var defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');

    function addGrad(id, c1, c2) {
      var g = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
      g.setAttribute('id', id); g.setAttribute('x1','0'); g.setAttribute('y1','0'); g.setAttribute('x2','1'); g.setAttribute('y2','0');
      var s1 = document.createElementNS('http://www.w3.org/2000/svg', 'stop'); s1.setAttribute('offset','0%'); s1.setAttribute('stop-color',c1);
      var s2 = document.createElementNS('http://www.w3.org/2000/svg', 'stop'); s2.setAttribute('offset','100%'); s2.setAttribute('stop-color',c2);
      g.appendChild(s1); g.appendChild(s2);
      return g;
    }
    defs.appendChild(addGrad('gInternal', '#2f9db6', '#287eb4'));
    defs.appendChild(addGrad('gLeaf', '#ffffff', '#edf8f7'));
    defs.appendChild(addGrad('gRoot', '#477ce1', '#315ecb'));
    defs.appendChild(addGrad('gBranch', '#72bcd0', '#438fd0'));

    var flt = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
    flt.setAttribute('id','shadow'); flt.setAttribute('x','-20%'); flt.setAttribute('y','-20%'); flt.setAttribute('width','140%'); flt.setAttribute('height','140%');
    var fd = document.createElementNS('http://www.w3.org/2000/svg', 'feDropShadow');
    fd.setAttribute('dx','0'); fd.setAttribute('dy','3'); fd.setAttribute('stdDeviation','4'); fd.setAttribute('flood-color','#215b99'); fd.setAttribute('flood-opacity','0.18');
    flt.appendChild(fd); defs.appendChild(flt);

    var glowFlt = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
    glowFlt.setAttribute('id','glow'); glowFlt.setAttribute('x','-30%'); glowFlt.setAttribute('y','-30%'); glowFlt.setAttribute('width','160%'); glowFlt.setAttribute('height','160%');
    var blur = document.createElementNS('http://www.w3.org/2000/svg', 'feGaussianBlur');
    blur.setAttribute('stdDeviation','3'); blur.setAttribute('result','blur');
    var merge = document.createElementNS('http://www.w3.org/2000/svg', 'feMerge');
    var mn1 = document.createElementNS('http://www.w3.org/2000/svg', 'feMergeNode'); mn1.setAttribute('in','blur');
    var mn2 = document.createElementNS('http://www.w3.org/2000/svg', 'feMergeNode'); mn2.setAttribute('in','SourceGraphic');
    merge.appendChild(mn1); merge.appendChild(mn2);
    glowFlt.appendChild(blur); glowFlt.appendChild(merge);
    defs.appendChild(glowFlt);

    svg.appendChild(defs);

    var edgeG = document.createElementNS('http://www.w3.org/2000/svg', 'g'); svg.appendChild(edgeG);
    var nodeG = document.createElementNS('http://www.w3.org/2000/svg', 'g'); svg.appendChild(nodeG);
    var effectG = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    effectG.setAttribute('aria-hidden', 'true');
    svg.appendChild(effectG);

    function playNodeClickEffect(nd, inner, rect) {
      if (reduceMotion) {
        rect.animate([
          { opacity: 1 },
          { opacity: 0.72 },
          { opacity: 1 }
        ], { duration: 260, easing: 'ease-out' });
        return;
      }

      var burst = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      burst.classList.add('tree-click-effect');
      burst.setAttribute('transform', 'translate(' + nd._x + ',' + nd._y + ')');
      effectG.appendChild(burst);

      var palette = nd._isRoot
        ? ['#3766d4', '#6c94eb', '#8cb8ff']
        : (nd._isLeaf ? ['#42a99d', '#7acfc3', '#85bdea'] : ['#258db2', '#54bfd0', '#6d93e5']);

      var halo = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      halo.setAttribute('cx', '0'); halo.setAttribute('cy', '0');
      halo.setAttribute('r', Math.max(nd._hp * 0.52, 22));
      halo.setAttribute('fill', 'none');
      halo.setAttribute('stroke', palette[0]);
      halo.setAttribute('stroke-width', '2');
      halo.style.transformBox = 'fill-box';
      halo.style.transformOrigin = 'center';
      burst.appendChild(halo);
      halo.animate([
        { opacity: 0.78, transform: 'scale(0.72)', strokeWidth: '2.5px' },
        { opacity: 0.34, offset: 0.58 },
        { opacity: 0, transform: 'scale(1.82)', strokeWidth: '0.7px' }
      ], { duration: 720, easing: 'cubic-bezier(0.18, 0.72, 0.3, 1)', fill: 'forwards' });

      var particleCount = 10;
      for (var k = 0; k < particleCount; k++) {
        var angle = (Math.PI * 2 * k / particleCount) + (nd._growOrder * 0.19);
        var distance = 26 + (k % 3) * 7;
        var px = Math.cos(angle) * distance;
        var py = Math.sin(angle) * distance * 0.72;
        var particle = document.createElementNS('http://www.w3.org/2000/svg', k % 3 === 0 ? 'path' : 'circle');
        if (k % 3 === 0) {
          particle.setAttribute('d', 'M0 -3.5 L3.5 0 L0 3.5 L-3.5 0 Z');
        } else {
          particle.setAttribute('cx', '0'); particle.setAttribute('cy', '0');
          particle.setAttribute('r', k % 2 ? '2.2' : '1.7');
        }
        particle.setAttribute('fill', palette[k % palette.length]);
        particle.style.transformBox = 'fill-box';
        particle.style.transformOrigin = 'center';
        burst.appendChild(particle);
        particle.animate([
          { opacity: 0, transform: 'translate(0, 0) scale(0.25)' },
          { opacity: 0.95, transform: 'translate(' + (px * 0.58) + 'px, ' + (py * 0.58) + 'px) scale(1)', offset: 0.38 },
          { opacity: 0, transform: 'translate(' + px + 'px, ' + py + 'px) scale(0.35)' }
        ], {
          duration: 560 + (k % 3) * 80,
          delay: k * 18,
          easing: 'cubic-bezier(0.2, 0.75, 0.28, 1)',
          fill: 'forwards'
        });
      }

      if (!introInProgress) {
        inner.animate([
          { transform: 'scale(1)', filter: 'brightness(1)' },
          { transform: 'scale(0.975)', filter: 'brightness(1.03)', offset: 0.22 },
          { transform: 'scale(1.055)', filter: 'brightness(1.12)', offset: 0.54 },
          { transform: 'scale(1)', filter: 'brightness(1)' }
        ], { duration: 460, easing: 'cubic-bezier(0.22, 0.8, 0.28, 1)' });
      }

      window.setTimeout(function() {
        if (burst.parentNode) burst.parentNode.removeChild(burst);
      }, 900);
    }

    // Edges (branch-like bezier curves) + leaf decorations
    for (var i = 0; i < nodes.length; i++) {
      var p = nodes[i];
      if (p.children) {
        for (var j = 0; j < p.children.length; j++) {
          var c = p.children[j];
          var x1 = p._x + p._w / 2, y1 = p._y;
          var x2 = c._x - c._w / 2, y2 = c._y;
          var dx = x2 - x1, cp = dx * 0.45;

          // Main branch
          var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path.setAttribute('d', 'M' + x1 + ' ' + y1 + ' C' + (x1+cp) + ' ' + y1 + ' ' + (x2-cp) + ' ' + y2 + ' ' + x2 + ' ' + y2);
          path.setAttribute('stroke', p._isRoot ? '#7395da' : '#83b9c6');
          path.setAttribute('stroke-width', p._isRoot ? '3' : '2');
          path.setAttribute('fill', 'none');
          path.setAttribute('stroke-linecap', 'round');
          path.setAttribute('opacity', '0.82');
          path.classList.add('tree-branch');
          edgeG.appendChild(path);

          // A subtle highlight keeps the branch airy on both light and dark displays.
          var path2 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path2.setAttribute('d', 'M' + x1 + ' ' + (y1-1) + ' C' + (x1+cp) + ' ' + (y1-1) + ' ' + (x2-cp) + ' ' + (y2-1) + ' ' + x2 + ' ' + (y2-1));
          path2.setAttribute('stroke', '#d9eff9');
          path2.setAttribute('stroke-width', '0.75');
          path2.setAttribute('fill', 'none');
          path2.setAttribute('stroke-linecap', 'round');
          path2.setAttribute('opacity', '0.72');
          path2.classList.add('tree-branch');
          edgeG.appendChild(path2);

          // A small bud marks the moment a growing branch reaches its node.
          var bud = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          bud.setAttribute('cx', x2); bud.setAttribute('cy', y2);
          bud.setAttribute('r', c._isLeaf ? '2.75' : '3.25');
          bud.setAttribute('fill', c._isLeaf ? '#67bdb1' : '#4599bc');
          bud.setAttribute('opacity', '0.85');
          bud.classList.add('tree-bud');
          edgeG.appendChild(bud);

          if (shouldAnimateIntro) {
            var branchDelay = 260 + (c._growOrder * 430);
            var branchDuration = 520;
            var branchLength = path.getTotalLength();
            path.style.setProperty('--branch-length', branchLength);
            path.style.strokeDasharray = branchLength;
            path.style.animation = 'branchGrow ' + branchDuration + 'ms cubic-bezier(0.34, 0.08, 0.28, 1) ' + branchDelay + 'ms both';
            path2.style.setProperty('--branch-length', branchLength);
            path2.style.strokeDasharray = branchLength;
            path2.style.animation = 'branchGrow ' + branchDuration + 'ms cubic-bezier(0.34, 0.08, 0.28, 1) ' + branchDelay + 'ms both';
            bud.style.opacity = '0';
            bud.style.animation = 'budPulse 360ms ease-out ' + (branchDelay + branchDuration - 80) + 'ms both';
          }

        }
      }
    }

    // Nodes
    for (var i = 0; i < nodes.length; i++) {
      (function(nd, idx) {
        var outer = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        outer.classList.add('tree-node');
        outer.setAttribute('transform', 'translate(' + (nd._x - nd._w/2) + ',' + (nd._y - nd._hp/2) + ')');
        outer.style.cursor = 'pointer';
        outer.setAttribute('tabindex', '0');
        outer.setAttribute('role', 'button');
        outer.setAttribute('aria-label', nd.name + '. Activate for a visual effect; hover for details.');

        var inner = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        inner.classList.add('tree-node-inner');
        if (shouldAnimateIntro) {
          var nodeDelay = nd._isRoot ? 80 : 700 + (nd._growOrder * 430);
          inner.style.opacity = '0';
          inner.style.animation = 'nodeGrowIn 620ms cubic-bezier(0.22, 0.9, 0.3, 1.18) ' + nodeDelay + 'ms both';
          inner.addEventListener('animationend', function onGrowthEnd(e) {
            if (e.animationName !== 'nodeGrowIn') return;
            inner.style.opacity = '1';
            inner.style.animation = 'none';
            inner.removeEventListener('animationend', onGrowthEnd);
          });
        } else {
          inner.style.animation = 'none';
        }
        outer.appendChild(inner);

        var rx = nd._isRoot ? 16 : (nd._isLeaf ? 11 : 14);
        var gradId = nd._isRoot ? 'url(#gRoot)' : (nd._isLeaf ? 'url(#gLeaf)' : 'url(#gInternal)');
        var strokeCol = nd._isRoot ? '#294fad' : (nd._isLeaf ? '#add8d2' : '#23749d');

        var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('width', nd._w); rect.setAttribute('height', nd._hp);
        rect.setAttribute('rx', rx); rect.setAttribute('ry', rx);
        rect.setAttribute('fill', gradId);
        rect.setAttribute('stroke', strokeCol);
        rect.setAttribute('stroke-width', nd._isLeaf ? '1.25' : '1.5');
        rect.setAttribute('filter', 'url(#shadow)');
        rect.classList.add('node-rect');
        inner.appendChild(rect);

        // A restrained leading mark makes the three hierarchy levels readable
        // without turning the nodes into buttons or badges.
        if (!nd._isLeaf) {
          var accent = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
          accent.setAttribute('x', '9'); accent.setAttribute('y', nd._hp/2 - 9);
          accent.setAttribute('width', '3'); accent.setAttribute('height', '18');
          accent.setAttribute('rx', '1.5');
          accent.setAttribute('fill', 'rgba(255,255,255,0.72)');
          inner.appendChild(accent);
        } else {
          var leafMark = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          leafMark.setAttribute('cx', '15'); leafMark.setAttribute('cy', nd._hp/2);
          leafMark.setAttribute('r', '4');
          leafMark.setAttribute('fill', '#64b9ae');
          leafMark.setAttribute('opacity', '0.9');
          inner.appendChild(leafMark);
        }

        var topLine = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        topLine.setAttribute('d', 'M' + rx + ' 1 H' + (nd._w-rx));
        topLine.setAttribute('stroke', nd._isLeaf ? 'rgba(255,255,255,0.95)' : 'rgba(255,255,255,0.32)');
        topLine.setAttribute('stroke-width', '1');
        topLine.setAttribute('stroke-linecap', 'round');
        topLine.setAttribute('pointer-events', 'none');
        inner.appendChild(topLine);

        var txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txt.setAttribute('x', nd._w/2 + 7); txt.setAttribute('y', nd._hp/2);
        txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('dy', '0.35em');
        txt.setAttribute('font-size', nd._isLeaf ? '11.3' : (nd._isRoot ? '13.2' : '12.2'));
        txt.setAttribute('font-weight', nd._isLeaf ? '600' : '700');
        txt.setAttribute('fill', nd._isLeaf ? '#315f68' : '#fff');
        txt.setAttribute('letter-spacing', nd._isRoot ? '0.2' : '0');
        txt.setAttribute('font-family', '"Trebuchet MS", Helvetica, sans-serif');
        txt.setAttribute('pointer-events', 'none');
        txt.textContent = nd.name;
        inner.appendChild(txt);

        outer.addEventListener('mouseenter', function(e) {
          var s = 1.045;
          var dw = nd._w * (s-1)/2, dh = nd._hp * (s-1)/2;
          outer.setAttribute('transform', 'translate(' + (nd._x - nd._w/2 - dw) + ',' + (nd._y - nd._hp/2 - dh) + ') scale(' + s + ')');
          rect.setAttribute('filter', 'url(#glow)');
          popoverTitle.textContent = nd.name;
          popoverBody.textContent = nd.details || 'No details yet. Edit treeData in _pages/about.md.';
          popover.style.display = 'block';
          popover.style.left = (e.clientX + 20) + 'px';
          popover.style.top = (e.clientY + 10) + 'px';
        });
        outer.addEventListener('mousemove', function(e) {
          popover.style.left = (e.clientX + 20) + 'px';
          popover.style.top = (e.clientY + 10) + 'px';
        });
        outer.addEventListener('mouseleave', function() {
          outer.setAttribute('transform', 'translate(' + (nd._x - nd._w/2) + ',' + (nd._y - nd._hp/2) + ')');
          rect.setAttribute('filter', 'url(#shadow)');
          popover.style.display = 'none';
        });
        outer.addEventListener('click', function() {
          playNodeClickEffect(nd, inner, rect);
        });
        outer.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            playNodeClickEffect(nd, inner, rect);
          }
        });

        nodeG.appendChild(outer);
      })(nodes[i], i);
    }

    if (shouldAnimateIntro) {
      introInProgress = true;
      introHasPlayed = true;
      window.setTimeout(function() {
        introInProgress = false;
        if (resizeQueuedDuringIntro) {
          resizeQueuedDuringIntro = false;
          render();
        }
      }, 4200);
    } else {
      introHasPlayed = true;
    }
  }

  render();
  window.addEventListener('resize', function() {
    if (introInProgress) {
      resizeQueuedDuringIntro = true;
      return;
    }
    clearTimeout(window._treeResizeTimer);
    window._treeResizeTimer = setTimeout(render, 200);
  });
})();
</script>

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/publications/NSD.png' alt="NSD" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Negative Self-Distillation: Learning to Reason by Avoiding Flaws](https://arxiv.org/pdf/2609.11699)

**Rongcan Pei**, Zhepei Wei, Shuyao Xu, Xinyu Zhu, Wei-Lin Chen, Yu Meng

[**arXiv**](https://arxiv.org/pdf/2609.11699)
- We propose **Negative Self-Distillation (NSD)**, which improves LLM reasoning by learning to avoid errors produced by a negatively conditioned version of the model, without requiring reference answers or an external teacher. A **dynamic token-level gate** directs training toward reasoning errors while protecting basic language abilities. Across seven mathematical reasoning benchmarks, NSD improves average accuracy by **2.3, 7.5, and 6.0 percentage points** for 1.7B, 4B, and 8B models, respectively, while retaining self-correction and improving training efficiency.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2026</div><img src='images/publications/VERA.png' alt="VERA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VERA: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding](https://arxiv.org/abs/2602.10146v1)

**Rongcan Pei**, Huan Li, Fang Guo, Qi Zhu

[**Code**](https://github.com/Prongcan/VERA) \| [**arXiv**](https://arxiv.org/abs/2602.10146v1)
- Through attention analysis, we identify specific **Visual Evidence Retrieval (VER) Heads** — a *sparse, dynamic* set of attention heads critical for locating visual cues during reasoning. We propose **VERA**, a training-free framework that detects model uncertainty to trigger explicit verbalization of visual evidence. VERA achieves **21.3%** relative improvement on Qwen3-VL-8B-Instruct and **20.1%** on GLM-4.1V-Thinking across five benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">COLM 2026 Workshop LM4Sci</div><img src='images/publications/instructor.png' alt="DeepInstructor" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation](https://openreview.net/pdf?id=SkakT0pnsL)

**Rongcan Pei***, Fang Guo*, Qinglin Qi, Qi Zhu, Yun Luo, Jianhao Yan, Minjun Zhu, Qiujie Xie, Dehong Zheng, Yue Zhang

[**Paper**](https://openreview.net/pdf?id=SkakT0pnsL) \| [**Code & Prompts**](https://github.com/Prongcan/ExpInstructor)
- We propose **DeepInstructor**, the first agentic AI instructor that emulates how human mentors leverage past scholarly experience to guide research ideation. DeepInstructor extracts experience triples from large-scale review corpora, constructs an Experience Graph, and employs an agentic reasoning framework for experience-driven idea evaluation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/publications/paperignition.png' alt="PaperIgnition" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PaperIgnition & Sci-Surf Project](https://arxiv.org/pdf/2608.11973)

Qi Zhu*, Fang Guo*, **Rongcan Pei***, Shuqi He, Hui Chen, Yue Zhang

[**arXiv**](https://arxiv.org/pdf/2608.11973) \| [**Website**](http://www.paperignition.com/) \| [**Code**](https://github.com/Algnite-Solutions/PaperIgnition)
- An intelligent paper recommendation and digestion platform that adopts a temporally decoupled architecture. The system autonomously fetches, indexes, and digests newly released arXiv papers through a daily pipeline, with multimodal LLM-based summarization executed offline.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISSTA 2026</div><img src='images/publications/issta.png' alt="ELSA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Augmenting Multi-Technique Static Analysis with Large Language Models: A Neuro-Symbolic Approach to Smart Contract Vulnerability Detection](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/131/Augmenting-Multi-Technique-Static-Analysis-with-Large-Language-Models-A-Neuro-Symbol)

Junxiang Wang, Fu Song, **Miaomiao Zhang**, Bowen Du, **Rongcan Pei**

- We propose **ELSA**, a neuro-symbolic approach that augments static analysis with LLM-assisted constraint-guided reasoning and resolves conflicting outputs through analyzer ensemble. ELSA significantly outperforms baselines across three open-source benchmarks and self-constructed ZKP-based smart contracts.
</div>
</div>

# 🎖 Honors and Awards
- *2025*, Social Activity Scholarship, Tongji University.
- *2024*, Guo Xie Birong Scholarship (equivalent to University First-Class Scholarship), Tongji University.

# 📖 Educations
- *2023.09 - Present*, Undergraduate Student, Tongji University. Advised by Prof. **Miaomiao Zhang**.

# 💻 Service
- Invited as reviewer for **KDD 2026**.

# 💻 Experience
<ul id="experience-list">
  <li><img src="{{ '/images/experience/ant-group.svg' | relative_url }}" alt="" loading="lazy"><span><em>2026.09 - Present</em>, AI Researcher (Intern), Ant Group.</span></li>
  <li><img class="experience-logo-wide" src="{{ '/images/experience/university-of-virginia.svg' | relative_url }}" alt="" loading="lazy"><span><em>2026.04 - Present</em>, Research Intern, University of Virginia. Advised by Prof. <a href="https://yumeng5.github.io/"><strong>Yu Meng</strong></a>.</span></li>
  <li><img class="experience-logo-westlake" src="{{ '/images/experience/westlake-university.png' | relative_url }}" alt="" loading="lazy"><span><em>2025.04 - 2026.05</em>, Visiting Student, Westlake University. Advised by Prof. <a href="https://frcchang.github.io/"><strong>Yue Zhang</strong></a>.</span></li>
  <li><img class="experience-logo-zju" src="{{ '/images/experience/zhejiang-university.png' | relative_url }}" alt="" loading="lazy"><span><em>2025.04 - Present</em>, Research Collaborator, Zhejiang University. Advised by Prof. <a href="https://gentlezhu.github.io/"><strong>Qi Zhu</strong></a>.</span></li>
</ul>
