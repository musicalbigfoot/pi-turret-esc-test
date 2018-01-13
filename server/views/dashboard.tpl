% include('_header.tpl', title=title)

<main class="dashboard">
	<h1>{{title}}</h1>

	<form data-control="dashboard">
		
		<div class="flex-wrapper">

			<section data-section="speed">
				
				<h2 class="section-title">Sauce</h2>

				<div class="speed-input__wrapper">
					<div class="speed-input__container">
						<div class="speed-input__input">
							<input type="radio" name="speed" value="mild" class="mild" id="speed--mild" checked="checked">
							<label for="speed--mild" class="mild"></label>
						</div>
						<div class="speed-input__label">
							<label for="speed--mild">Mild</label>
						</div>
					</div>

					<div class="speed-input__container">
						<div class="speed-input__input">
							<input type="radio" name="speed" value="medium" class="medium" id="speed--medium">
							<label for="speed--medium" class="medium"></label>
						</div>
						<div class="speed-input__label">
							<label for="speed--medium">Medium</label>
						</div>
					</div>

					<div class="speed-input__container">
						<div class="speed-input__input">
							<input type="radio" name="speed" value="hot" class="hot" id="speed--hot">
							<label for="speed--hot" class="hot"></label>
						</div>
						<div class="speed-input__label">
							<label for="speed--hot">Hot</label>
						</div>
					</div>
				</div>

			</section>

			<section data-section="shots">
				
				<h2 class="section-title">Shots</h2>

				<div class="shots-input__container">
					<button class="shots-input__button shots-input__button--down">-</button>
					<input type="number" name="shots" id="shots-input__input" class="shots-input__input" value="1" min="1" max="18">
					<button class="shots-input__button shots-input__button--up">+</button>
				</div>

			</section>

		</div>

		<aside class="status">
			<input type="text" id="fire-safety" required="required">
			<button type="submit">Fire!</button>
		</aside>

	</form>
</main>

% include('_footer.tpl')