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
- <strong style="color: #c62828;">📌 Pinned: I am looking for PhD opportunities for Fall 2027!</strong>
- *2026.09*: &nbsp;🚀 We propose [**NSD**](https://arxiv.org/pdf/2609.11699), our new work on improving LLM reasoning through negative self-distillation!
- *2026.08*: &nbsp;🌍✈️ Attended **IJCAI 2026** in beautiful **Bremen, Germany**!
- *2026.07*: &nbsp;🎉 Our paper "DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation" has been accepted by **COLM 2026 Workshop LM4Sci**!
- *2026.05*: &nbsp;🎉 Our paper "VERA: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding" has been accepted by **IJCAI 2026**!
- *2026.04*: &nbsp;🎉 Our paper "Augmenting Multi-Technique Static Analysis with Large Language Models" has been accepted by **ISSTA 2026**!

# 🌳 My Experience Tree

I am committed to comprehensively understanding and researching the full pipeline of LLM training and inference. Below is my experience tree.

<style>
#experience-tree-container {
  width: 100%;
  overflow-x: auto;
  margin: 1.5em 0;
  padding: 10px 0;
}
#experience-tree {
  width: 100%;
  min-height: 400px;
  display: block;
}
#experience-tree .node-rect {
  transition: filter 0.25s ease;
}
#experience-tree .node-text {
  font-family: "Trebuchet MS", Helvetica, sans-serif;
  pointer-events: none;
  user-select: none;
}
@keyframes float1 {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}
@keyframes float2 {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-3px); }
}
.tree-popover {
  position: fixed;
  background: #fff;
  border: 1px solid #c8e0c8;
  border-radius: 8px;
  padding: 14px 18px;
  max-width: 380px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.14);
  z-index: 9999;
  display: none;
  font-family: "Trebuchet MS", Helvetica, sans-serif;
  pointer-events: none;
}
.tree-popover-title {
  font-weight: bold;
  color: #3a7a3a;
  font-size: 14px;
  margin-bottom: 6px;
}
.tree-popover-body {
  color: #555;
  font-size: 13px;
  line-height: 1.65;
}
</style>

<div id="experience-tree-container">
  <svg id="experience-tree"></svg>
</div>
<div class="tree-popover" id="tree-popover">
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
          { name: "Post Training", details: "Negative Self-Distillation (NSD) shows that self-improvement can come from learning which reasoning behaviors to avoid. A teacher conditioned on correct answers can encourage overconfidence and weaken self-correction. We construct a negative teacher from the model itself, then use dynamic token-level gating to target reasoning flaws while preserving basic language abilities. The key insight is that selective negative feedback can improve reasoning without ground-truth answers or an external teacher, while retaining exploration and self-correction." },
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
  var marginTop = 15;
  var marginBot = 15;
  var nodeH = 48;
  var leafH = 38;
  var textPad = 22;
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

  function render() {
    var cw = Math.max(container.clientWidth - 20, 750);
    computeLayout(treeData);
    var totalH = Math.max(treeData._h * (leafH + siblingGap) + marginTop + marginBot, 250);
    assignPositions(treeData, 0, marginTop, totalH - marginBot);

    // Compute centering offset
    var nodes = [];
    collectNodes(treeData, nodes);
    var minX = Infinity, maxX = -Infinity;
    for (var i = 0; i < nodes.length; i++) {
      var nd = nodes[i];
      nd._isLeaf = !nd.children || nd.children.length === 0;
      nd._isRoot = (nd === treeData);
      nd._w = textWidth(nd.name, nd._isLeaf ? 11 : (nd._isRoot ? 13.5 : 12.5));
      nd._hp = nd._isLeaf ? leafH : (nd._isRoot ? 52 : nodeH);
      if (nd._x - nd._w/2 < minX) minX = nd._x - nd._w/2;
      if (nd._x + nd._w/2 > maxX) maxX = nd._x + nd._w/2;
    }
    var treeWidth = maxX - minX;
    var offsetX = (cw - treeWidth) / 2 - minX;
    if (offsetX < 0) offsetX = 0;

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
    totalH = Math.max(newMaxY + marginBot, 250);

    svg.setAttribute('viewBox', '0 0 ' + totalW + ' ' + totalH);
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', totalH);
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
    defs.appendChild(addGrad('gInternal', '#72c472', '#4a9a4a'));
    defs.appendChild(addGrad('gLeaf', '#c8eac8', '#8dc88d'));
    defs.appendChild(addGrad('gRoot', '#4ea84e', '#2d702d'));
    defs.appendChild(addGrad('gBranch', '#7ab87a', '#5a985a'));

    var flt = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
    flt.setAttribute('id','shadow'); flt.setAttribute('x','-20%'); flt.setAttribute('y','-20%'); flt.setAttribute('width','140%'); flt.setAttribute('height','140%');
    var fd = document.createElementNS('http://www.w3.org/2000/svg', 'feDropShadow');
    fd.setAttribute('dx','0'); fd.setAttribute('dy','2'); fd.setAttribute('stdDeviation','3'); fd.setAttribute('flood-color','rgba(0,0,0,0.10)');
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
          path.setAttribute('stroke', '#8ab88a');
          path.setAttribute('stroke-width', p._isRoot ? '4' : '2.5');
          path.setAttribute('fill', 'none');
          path.setAttribute('stroke-linecap', 'round');
          path.setAttribute('opacity', '0.7');
          edgeG.appendChild(path);

          // Thinner highlight line on top
          var path2 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          path2.setAttribute('d', 'M' + x1 + ' ' + (y1-1) + ' C' + (x1+cp) + ' ' + (y1-1) + ' ' + (x2-cp) + ' ' + (y2-1) + ' ' + x2 + ' ' + (y2-1));
          path2.setAttribute('stroke', '#b0d8b0');
          path2.setAttribute('stroke-width', '1');
          path2.setAttribute('fill', 'none');
          path2.setAttribute('stroke-linecap', 'round');
          path2.setAttribute('opacity', '0.5');
          edgeG.appendChild(path2);

        }
      }
    }

    // Nodes
    for (var i = 0; i < nodes.length; i++) {
      (function(nd, idx) {
        var outer = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        outer.setAttribute('transform', 'translate(' + (nd._x - nd._w/2) + ',' + (nd._y - nd._hp/2) + ')');
        outer.style.cursor = 'pointer';

        var inner = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        var floatName = 'float' + (1 + idx % 2);
        var dur = 3 + idx * 0.4;
        inner.style.animation = floatName + ' ' + dur + 's ease-in-out infinite';
        inner.style.animationDelay = (idx * 0.35) + 's';
        outer.appendChild(inner);

        var rx = nd._hp / 2;
        var gradId = nd._isRoot ? 'url(#gRoot)' : (nd._isLeaf ? 'url(#gLeaf)' : 'url(#gInternal)');
        var strokeCol = nd._isRoot ? '#267026' : (nd._isLeaf ? '#6daa6d' : '#357a35');

        var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('width', nd._w); rect.setAttribute('height', nd._hp);
        rect.setAttribute('rx', rx); rect.setAttribute('ry', rx);
        rect.setAttribute('fill', gradId);
        rect.setAttribute('stroke', strokeCol);
        rect.setAttribute('stroke-width', nd._isLeaf ? '1.5' : '2');
        rect.setAttribute('filter', 'url(#shadow)');
        rect.classList.add('node-rect');
        inner.appendChild(rect);

        var txt = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        txt.setAttribute('x', nd._w/2); txt.setAttribute('y', nd._hp/2);
        txt.setAttribute('text-anchor', 'middle'); txt.setAttribute('dy', '0.35em');
        txt.setAttribute('font-size', nd._isLeaf ? '11.5' : (nd._isRoot ? '13.5' : '12.5'));
        txt.setAttribute('font-weight', nd._isLeaf ? 'normal' : 'bold');
        txt.setAttribute('fill', nd._isLeaf ? '#2d5a2d' : '#fff');
        txt.setAttribute('font-family', '"Trebuchet MS", Helvetica, sans-serif');
        txt.setAttribute('pointer-events', 'none');
        txt.textContent = nd.name;
        inner.appendChild(txt);

        outer.addEventListener('mouseenter', function(e) {
          var s = 1.12;
          var dw = nd._w * (s-1)/2, dh = nd._hp * (s-1)/2;
          outer.setAttribute('transform', 'translate(' + (nd._x - nd._w/2 - dw) + ',' + (nd._y - nd._hp/2 - dh) + ') scale(' + s + ')');
          inner.style.animation = 'none';
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
          inner.style.animation = floatName + ' ' + dur + 's ease-in-out infinite';
          rect.setAttribute('filter', 'url(#shadow)');
          popover.style.display = 'none';
        });

        nodeG.appendChild(outer);
      })(nodes[i], i);
    }
  }

  render();
  window.addEventListener('resize', function() { clearTimeout(window._treeResizeTimer); window._treeResizeTimer = setTimeout(render, 200); });
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
- *2026.04 - Present*, Research Intern, University of Virginia. Advised by Prof. [**Yu Meng**](https://yumeng5.github.io/).
- *2025.04 - 2026.05*, Visiting Student, Westlake University. Advised by Prof. [**Yue Zhang**](https://frcchang.github.io/).
- *2025.04 - Present*, Research Collaborator, Zhejiang University. Advised by Prof. [**Qi Zhu**](https://gentlezhu.github.io/).
